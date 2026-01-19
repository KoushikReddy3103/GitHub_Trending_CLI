from argparse import ArgumentParser,Namespace


parser = ArgumentParser(prog='GitHub Trending CLI', description='CLI tool will fetch data from the GitHub API', epilog="trending-repos --duration month --limit 20", suggest_on_error=True)

parser.add_argument("--duration", type=int, choices=["week","day","month","year"], default="week", required=True, help="Specifies the time i.e. `day`, `week`, `month`,`year`")
parser.add_argument("--limit", type=int, required=True, default=10, help="Specifies the number of repositories to display")

options = parser.parse_args(namespace = Namespace())




