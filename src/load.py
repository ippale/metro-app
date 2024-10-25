def init_db():
    import database.init as db
    db.init_db()


def parse_and_load():
    import parsers.house_parser as hp
    import parsers.metro_parser as mp

    import loaders.house_loader as hl
    import loaders.metro_loader as ml

    for house in hp.HouseParser("data/russian_houses_sample.csv").get_data():
        house_loader = hl.HouseLoader(house)
        house_loader.load()
    hl.HouseLoader()  # КОСТЫЛЬ

    for metro in mp.MetroParser("data/russian_metro_2.json").get_data():
        metro_loader = ml.MetroLoader(metro)
        metro_loader.load()


def update_stat():
    from database.aggregate import aggregate
    aggregate()


def main():
    # initialize database
    print("initializing database")
    init_db()
    print("complete")
    # read data from file and load to db
    print("parsing files and uploading into db")
    parse_and_load()
    print("complete")
    # create statistic
    print("updating statistics")
    update_stat()
    print("complete")
    print("To start api server type: python3 src/api.py")


if __name__ == '__main__':
    main()
