from typing import Any

from service import get_episode, get_show_id_range, download_data


def main():

    show_header()

    # DOWNLOAD THE EPISODE DATA
    download_data('https://talkpython.fm/episodes/rss')

    # GET LATEST SHOW ID
    latest_show_id, oldest_show_id = get_show_id_range()

    print("Working with total of {} episodes".format(latest_show_id))

    end: int | Any
    end, start = display_results(latest_show_id, oldest_show_id)

    for show_id in range(start, end):
        info = get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def display_results(latest_show_id, oldest_show_id):
    # DISPLAY RESULTS
    start = oldest_show_id
    end = latest_show_id + 1
    return end, start


def show_header():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
