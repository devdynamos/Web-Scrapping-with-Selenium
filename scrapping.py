
# IMPORTS SELENIUM

def save_in_excel(pic, name, dtype, number, highlight, bio, points):
    ...

def scrape_doctor(profile_link):
    # OPEN USER PROFILE IN NEW TAB

    profile_picture = "" # //div[@class="pic-stats--pic"]//img.get_attribute('src')

    name = "" # //div[@class="name-bio--name"]//h2
    doc_type = "" # //div[@class="name-bio--name"]//h4

    phone_number = "" # //a[@id="btn-profile_phone-view"].get_attribute('data')

    high_lights = "" # //div[@class="result-highlights"]//li --> Multiple
    bio = "" # //p[@class="p_bio"]

    profile_points = "" # //span[@class="current-count"].get_attribute('data-to')

    # CLOSE NEW TAB

    def save_in_excel(pic=profile_picture,
                      name=name,
                      dtype=doc_type,
                      number=phone_number,
                      highlight=high_lights,
                      bio=bio,
                      points=profile_points)

# GO TO https://www.doctor.com/90033/Family-Doctors
while True:
    cards = None
    # GET ALL LINKS USING XPATH //hgroup//a and save it in cards

    for card in cards:
        print(card.text)
        profile_link = card.get__attribute("href")

        scrape_doctor(profile_link)
    
    next_button = None
    # GET NEXT BUTTON USING XAPTH //li[@class="next"]
    
    if next_button:
        next_button.click()
    else:
        break
