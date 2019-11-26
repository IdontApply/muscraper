
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

    # r = []
    for sublist in results:

        psellers, pitemsinfo, pprices, plinks, prating,  ppages = sublist

        search2 = [search1] * 60

        pages.extend(ppages)
        sellers.extend(psellers)
        itemsinfo.extend(pitemsinfo)
        prices.extend(pprices)
        links.extend(plinks)
        rating.extend(prating)
        search.extend(search2)
    print(len(search))
    print('>>>>>\n')
    return list(zip(sellers, itemsinfo, prices, links, rating, pages, search)), sellers
