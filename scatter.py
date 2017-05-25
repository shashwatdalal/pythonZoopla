from zoopla import Zoopla
import matplotlib.pyplot as plt
from geopy.distance import vincenty
import matplotlib.patches as mpatches

zoopla = Zoopla(api_key='ubtyux3etedzj6td2af7zy6g', debug=False, wait_on_rate_limit=True)
housetTypes = ['furnished','unfurnished','part-furnished']
colors = ['g','y','r']
imperial = (51.498873,-0.175972)


for (houseType,color) in zip(housetypes,colors):
    search = zoopla.search_property_listings(params = {
        'minimum_beds'  : 4,
        'maximum_bed'   : 5,
        'listing_staus' : 'rent',
        'minimum_price' : 100*5,
        'maximum_price' : 200*5,  #per week in GBP
        'furnished'     : houseType,
        'latitude'      : '51.498873',
        'longitude'     : '-0.175972',
        'radius'        : 1,
        'page_size'     : 100
        })
   
    distance = [vincenty(imperial,(result.latitude,result.longitude)).kilometers for result in search]
    price = [result.price for result in search]
    plt.scatter(distance,price,c = color,marker = '.')

red_patch = mpatches.Patch(color='red', label='Furnished')
yellow_patch = mpatches.Patch(color='yellow', label='Part-Furnished')
green_patch = mpatches.Patch(color='green', label='Unfurnished')
plt.legend(handles = [red_patch,yellow_patch,green_patch])

plt.xlabel('Distance From Imperial (km)')
plt.ylabel('Price per Week (pounds)')
plt.show()
