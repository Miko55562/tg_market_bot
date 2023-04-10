import configparser

con = configparser.ConfigParser()
con.read('config.ini', encoding='utf-8')

course = con.get('DEFAULT', 'course').replace('\\n', '\n')
start_menu_button_1 = con.get('DEFAULT', 'start_menu_button_1').replace('\\n', '\n')
start_menu_button_2 = con.get('DEFAULT', 'start_menu_button_2').replace('\\n', '\n')
start_menu_button_3 = con.get('DEFAULT', 'start_menu_button_3').replace('\\n', '\n')
start_menu_button_4 = con.get('DEFAULT', 'start_menu_button_4').replace('\\n', '\n')
start_menu_button_5 = con.get('DEFAULT', 'start_menu_button_5').replace('\\n', '\n')
start_text_message = con.get('DEFAULT', 'start_text_message').replace('\\n', '\n')
start_menu_button_1_text_message = con.get('DEFAULT', 'start_menu_button_1_text_message', raw=True).replace('\\n', '\n')
start_menu_button_2_text_message = con.get('DEFAULT', 'start_menu_button_2_text_message', raw=True).replace('\\n', '\n')
ready_to_buy = con.get('DEFAULT', 'ready_to_buy', raw=True).replace('\\n', '\n')
price_calculation = con.get('DEFAULT', 'price_calculation', raw=True).replace('\\n', '\n')
faq_menu_button_1 = con.get('DEFAULT', 'faq_menu_button_1').replace('\\n', '\n')
faq_menu_button_2 = con.get('DEFAULT', 'faq_menu_button_2').replace('\\n', '\n')
faq_menu_button_3 = con.get('DEFAULT', 'faq_menu_button_3').replace('\\n', '\n')
faq_menu_button_4 = con.get('DEFAULT', 'faq_menu_button_4').replace('\\n', '\n')
faq_menu_button_5 = con.get('DEFAULT', 'faq_menu_button_5').replace('\\n', '\n')
faq_menu_text = con.get('DEFAULT', 'faq_menu_text').replace('\\n', '\n')
faq_menu_text_1 = con.get('DEFAULT', 'faq_menu_text_1').replace('\\n', '\n')
faq_menu_text_2 = con.get('DEFAULT', 'faq_menu_text_2').replace('\\n', '\n')
faq_menu_text_3 = con.get('DEFAULT', 'faq_menu_text_3').replace('\\n', '\n')
faq_menu_text_4 = con.get('DEFAULT', 'faq_menu_text_4').replace('\\n', '\n')
faq_menu_text_5 = con.get('DEFAULT', 'faq_menu_text_5').replace('\\n', '\n')
support_text = con.get('DEFAULT', 'support_text').replace('\\n', '\n')
support_url = con.get('DEFAULT', 'support_url').replace('\\n', '\n')
reviews = con.get('DEFAULT', 'reviews')
reviews_text = con.get('DEFAULT', 'reviews_text')


def edit_text(name, new_text):
    if not isinstance(name, str):
        name = str(name)
    con['DEFAULT'][name] = new_text.replace('%', '%%')


def get_text(name: str):
    if con is not None:
        return con.get('DEFAULT', name).replace('\\n', '\n')
    else:
        return None


def get_raw(name: str):
    if con is not None:
        return con.get('DEFAULT', name, raw=True).replace('\\n', '\n')
    else:
        return None


def save():
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        con.write(configfile)


token = ''
admin_id = ''
proxy_url = ''
