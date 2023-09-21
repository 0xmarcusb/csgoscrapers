import requests
import bs4
from bs4 import BeautifulSoup
import time
import csv
start_time = time.time()
names = [0]*10
namesend = ["error"]*10
nameslist = ["error"]*10
priceend = [0]*10
pricestart = [0]*10
pricelist = [0]*10
################################
# SOME SEARCH FUNCTION SEARCHING FOR THE START OF THE ITEM NAMES
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
################################
pagecheck = 1
pageamount = 10
namelist = []*10*pageamount
nameslistend = []
pricelistend = []
allpagenames=[]*10*pageamount
allpricenames=[]*10*pageamount


print("Steam Scraper, scraping "+str(pageamount)+"pages, or "+str(10*pageamount)+"items")
while pagecheck < pageamount+1:
    namelist = []*10*pageamount
    nameslistend = []
    pricelistend = []
    URL = "https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730&q=capsule"
    #URL = "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_normal&category_730_Quality%5B%5D=tag_strange&category_730_Rarity%5B%5D=tag_Rarity_Common_Weapon&category_730_Rarity%5B%5D=tag_Rarity_Rare_Weapon&category_730_Rarity%5B%5D=tag_Rarity_Uncommon_Weapon&category_730_Rarity%5B%5D=tag_Rarity_Mythical_Weapon&category_730_Rarity%5B%5D=tag_Rarity_Legendary_Weapon&appid=730#p"+str(pagecheck)+"_popular_desc" 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    atag = str(soup.find_all("a"))
    #print(atag)
    check = 0
    while check<10:
        names[check] = (find_nth(atag, "data-hash-name", check))+16
        namesend[check] = (find_nth(atag[names[check]:],"\"",1))
        nameslist[check] = (atag[names[check]:namesend[check]+names[check]])
        pricestart[check] = (find_nth(atag, "$", check))
        priceend[check] = (find_nth(atag[pricestart[check]:]," ",1))
        pricelist[check] = (atag[pricestart[check]:priceend[check]+pricestart[check]])
        check = check+1
    allpagenames[10*(pagecheck+1)-10:10*(pagecheck+1)] = nameslist[0:10]
    allpricenames[10*(pagecheck+1)-10:10*(pagecheck+1)] = pricelist[0:10]
    
    
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    nameslistend.append(nameslist)
    pricelistend.append(pricelist)
    pagecheck = pagecheck +1
    
    
print(allpricenames)
#print(allpagenames)
print(len(allpagenames))

with open('/Users/marcus/Documents/csgo.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(nameslistend)
    writer.writerow(pricelistend)

#second stage

check = 0
while check < len(allpagenames):
    curstring = allpagenames[check]
    curstring  = curstring.replace(" ","%20")
    #print(curstring)
    allpagenames[check] = curstring
    check = check+1
print(allpagenames)





