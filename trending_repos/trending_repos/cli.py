import argparse
import sys
import logging
from trending_repos.github_api import fetch_repositories, GitHubAPIError
from trending_repos.utils import get_start_date, DURATION_MAP


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch trending GitHub repositories"
    )

    parser.add_argument(
        "--duration",
        choices=DURATION_MAP.keys(),
        default="week",
        help="Time range for trending repositories (default: week)",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
           help="Number of repositories to display (default: 10)",
    )

    return parser.parse_args()


def display_repositories(repositories):
    logger.info("\n Trending GitHub Repositories\n")

    for idx, repo in enumerate(repositories, start=1):
        name= repo.get("full_name", "N/A")
        description = repo.get("description") or "No description"
        stars = repo.get("stargazers_count", 0)
        language = repo.get("language") or "Unknown"

        logger.info(f"{idx}. {name}")
        logger.info(f"   ⭐Stars : {stars}")
        logger.info(f"   🧠 Language : {language}")
        logger.info(f"   📄 {description}")
        logger.info("-" * 60)


def main():
    args = parse_arguments()

    if args.limit <= 0:
        logger.error("❌ --limit must be a positive integer")
        sys.exit(1)
    
    try:
        start_date = get_start_date(args.duration)
        repositories = fetch_repositories(start_date, args.limit)
        display_repositories(repositories)
    
    except ValueError as exc:
        logger.error(f"❌ {exc}")
        sys.exit(1)
    
    except GitHubAPIError as exc:
        logger.error(f"❌ API Error: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    main()
