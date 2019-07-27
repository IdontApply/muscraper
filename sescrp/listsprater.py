
def list_sprater(results, search1):

    print('list_sprater>>>>>\n')
    print(search1)

    sellers = []
    itemsinfo = []
    prices = []
    links = []
    rating = []
    pages = []
    search = []

    r = []
    for sublist in results:

        Psellers, Pitemsinfo, Pprices, Plinks, Prating,  Ppages= sublist

        search2 = [search1] * 60

        pages.extend(Ppages)
        sellers.extend(Psellers)
        itemsinfo.extend(Pitemsinfo)
        prices.extend(Pprices)
        links.extend(Plinks)
        rating.extend(Prating)
        search.extend(search2)
    print(len(search))
    print('>>>>>\n')
    return list(zip(sellers, itemsinfo, prices, links, rating, pages, search)) , sellers
