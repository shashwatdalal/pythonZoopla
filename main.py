from zoopla import Zoopla
import gmplot

zoopla = Zoopla(api_key='ubtyux3etedzj6td2af7zy6g', debug=False, wait_on_rate_limit=True)

search = zoopla.search_property_listings(params = {
    'minimum_beds'  : 4,
    'maximum_bed'   : 5,
    'listing_staus' : 'rent',
    'minimum_price' : 150*5,
    'maximum_price' : 200*5,  #per week in GBP
    #'furnished'     : 'furnished',
    'latitude'      : '51.498873',
    'longitude'     : '-0.175972',
    'radius'        : 1.5,
    'house_type'    : 'house',
    'page_size'     : 100
    })

for result in search:
    print(result.price)
    print(result.description)
    print(result.details_url)

gmap = gmplot.GoogleMapPlotter(51.4820096, -0.1971278, 14)
gmap.scatter([result.latitude for result in search],
             [result.longitude for result in search],
             '#3B0B39', size=10, marker=False)

gmap.draw("mymap.html")
