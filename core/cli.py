"""
Commandline interface
"""
import asyncio
import logging
import os
import platform
import sys

from argparse import ArgumentParser, RawDescriptionHelpFormatter

from .core import *
from .report import *
from .server import *


logging.basicConfig(format='[%(asctime)s][%(levelname)s][%(filename)s:%(funcName)s():%(lineno)d]:\t %(message)s')


def setup_arguments_parser():
    from aiohttp import __version__ as aiohttp_version
    from ._version import __version__

    version_string = '\n'.join(
        [
            f'%(prog)s {__version__}',
            f'Python:  {platform.python_version()}',
            f'Aiohttp:  {aiohttp_version}',
        ]
    )

    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=f"OSINT tool v{__version__}\n"
    )
    target_group = parser.add_argument_group(
        'INPUT', 'Options for input data'
    )
    target_group.add_argument(
        "target",
        nargs='*',
        metavar="TARGET",
        help="One or more target to get info by.",
    )
    target_group.add_argument(
        "--target-list",
        action="store",
        dest="target_list_filename",
        default='',
        help="Path to text file with list of targets.",
    )
    target_group.add_argument(
        "--targets-from-stdin",
        action="store_true",
        dest="target_list_stdin",
        default=False,
        help="Read all the lines from standard input.",
    )
    out_group = parser.add_argument_group(
        'OUTPUT', 'Options for output reports'
    )
    out_group.add_argument(
        "--csv-report",
        "-oC",
        action="store",
        dest="csv_filename",
        default='',
        help="Path to file for saving CSV report.",
    )
    out_group.add_argument(
        "--text-report",
        "-oT",
        action="store",
        dest="txt_filename",
        default='',
        help="Path to file for saving TXT report (grepable console output).",
    )
    out_group.add_argument(
        "--json-report",
        "-oJ",
        action="store",
        dest="json_filename",
        default='',
        help="Path to file for saving JSON report.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=version_string,
        help="Display version information and dependencies.",
    )
    parser.add_argument(
        "--timeout",
        action="store",
        metavar='TIMEOUT',
        dest="timeout",
        default=100,
        help="Time in seconds to wait for execution.",
    )
    parser.add_argument(
        "--cookie-jar-file",
        metavar="COOKIE_FILE",
        dest="cookie_file",
        default='',
        help="File with cookies.",
    )
    parser.add_argument(
        "--proxy",
        "-p",
        metavar='PROXY_URL',
        action="store",
        dest="proxy",
        default='',
        help="Make requests over a proxy. e.g. socks5://127.0.0.1:1080",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        dest="verbose",
        default=False,
        help="Display extra information and metrics.",
    )
    parser.add_argument(
        "--silent",
        "-s",
        action="store_true",
        dest="silent",
        default=False,
        help="Suppress console output.",
    )
    parser.add_argument(
        "--info",
        "-vv",
        action="store_true",
        dest="info",
        default=False,
        help="Display extra/service information and metrics.",
    )
    parser.add_argument(
        "--debug",
        "-vvv",
        "-d",
        action="store_true",
        dest="debug",
        default=False,
        help="Display extra/service/debug information and metrics, save responses in debug.log.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        dest="no_color",
        default=False,
        help="Don't color terminal output",
    )
    parser.add_argument(
        "--no-progressbar",
        action="store_true",
        dest="no_progressbar",
        default=False,
        help="Don't show progressbar.",
    )
    parser.add_argument(
        "--server",
        metavar='SERVER_ADDR',
        action="store",
        dest="server",
        default='',
        help="Start a server on a specific IP:PORT. e.g. 0.0.0.0:8080",
    )

    return parser


async def main():
    # Logging
    log_level = logging.ERROR
    logging.basicConfig(
        format='[%(filename)s:%(lineno)d] %(levelname)-3s  %(asctime)s %(message)s',
        datefmt='%H:%M:%S',
        level=log_level,
    )
    logger = logging.getLogger('osint-cli-tool-skeleton')
    logger.setLevel(log_level)

    arg_parser = setup_arguments_parser()
    args = arg_parser.parse_args()

    if args.debug:
        log_level = logging.DEBUG
    elif args.info:
        log_level = logging.INFO
    elif args.verbose:
        log_level = logging.WARNING

    logger.setLevel(log_level)

    # server
    if args.server:
        await CheckServer(
            proxy=args.proxy,
            addr=args.server,
            loop=asyncio.get_event_loop(),
        ).start(debug=args.debug)

    input_data = []

    # read from file
    if args.target_list_filename:
        if not os.path.exists(args.target_list_filename):
            print(f'There is no file {args.target_list_filename}')
        else:
            with open(args.target_list_filename) as f:
                input_data = [InputData(t) for t in f.read().splitlines()]

    # or read from stdin
    # e.g. cat list.txt | ./run.py --targets-from-stdin
    elif args.target_list_stdin:
        for line in sys.stdin:
            input_data.append(InputData(line.strip()))

    # or read from arguments
    elif args.target:
        input_data = [InputData(t) for t in args.target]

    if not input_data:
        print('There are no targets to check!')
        sys.exit(1)

    # convert input to output
    processor = Processor(
        no_progressbar=args.no_progressbar,
        proxy=args.proxy,
    )

    output_data = await processor.process(input_data)

    # console output
    if not args.silent:
        r = PlainOutput(output_data, colored=not args.no_color)
        print(r.put())

    # save CSV report
    if args.csv_filename:
        r = CSVOutput(output_data, filename=args.csv_filename)
        print(r.put())

    # save TXT report

    if args.txt_filename:
        r = TXTOutput(output_data, filename=args.txt_filename)
        print(r.put())

    # save JSON report
    if args.json_filename:
        r = JSONOutput(output_data, filename=args.json_filename)
        print(r.put())

    await processor.close()


def run():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    loop.close()


if __name__ == "__main__":
    run()