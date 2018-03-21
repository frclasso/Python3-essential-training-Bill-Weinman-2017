#!/usr/bin/python


def main():
    import datetime
    now = datetime.datetime.now()
    print(now)
    print('Year=',now.year,'Month=', now.month,'Day=', now.day,'-',now.hour,'hours',
          now.minute,'minutes',now.second,'seconds')


if __name__ == "__main__":main()