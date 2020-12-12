from selenium import webdriver
import MySQLdb
import traceback


driver = webdriver.Chrome(executable_path='C:/Users/Arjun Sharma/PycharmProjects/sourcefuse/driver/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
url = "http://sfwebhtml:t63KUfxL5vUyFLG4eqZNUcuRQ@sfwebhtml.sourcefuse.com/automation-form-demo-for-interview/"
driver.get(url)

input_fields = driver.find_elements_by_css_selector('.form-control')
labels = driver.find_elements_by_xpath('//label')
radio = driver.find_elements_by_css_selector("input.form-check-input");
for x in range(len(input_fields)):
    if input_fields[x].get_attribute('required') :

            print((labels[x].text))

# checking for radio button separately because they don't have similar html
# attributes as the text fields
if driver.find_element_by_xpath("//input[@id='yes']").get_attribute('required'):
    print(driver.find_element_by_xpath("//label[@for='relocate']").text)

print('Testcase 1 execution completed!')

print('Executing Testcase 2 & 3!!')

#in python there is only assert , there is no soft assert and hard assert
#assert is preferred to be used in try/except statements
for x in range(len(input_fields)):
    assert input_fields[x].is_displayed(), 'Fields are visible';
print('Assertion without try/except')

for x in range(len(input_fields)):
    try:
        assert input_fields[x].is_displayed(),'Fields are  visible'

    except AssertionError :
        print('Assertion Error with try/except')
print('Assertion with try/except')

#Testcase 4 submitting form using Xpath
print('Execution of Testcase 4')

element = driver.find_element_by_xpath('//*[@id="fnameInput"]/input').send_keys('Arjun')
element2 = driver.find_element_by_xpath('//*[@id="lnameInput"]/input').send_keys('Sharma')
element3 = driver.find_element_by_xpath('//*[@id="emailInput"]/input').send_keys('sharmaarjun2850@gmail.com')
element4 = driver.find_element_by_xpath('//*[@id="curCompanyInput"]/input').send_keys('Clicklabs')
element5 = driver.find_element_by_xpath('//*[@id="mobInput"]/input').send_keys('9855579616')
element6 = driver.find_element_by_xpath('//*[@id="DOBInput"]/div/input').send_keys('07/18/1993')
element7 = driver.find_element_by_xpath('//*[@id="positionInput"]/input').send_keys('Sr SDET')
element8 = driver.find_element_by_xpath('//*[@id="portfolioInput"]/input').send_keys('https://www.linkedin.com/in/arjun-sharma-1b6ba3a7/')
element9 = driver.find_element_by_xpath('//*[@id="salaryInput"]/input').send_keys('12lpa')
element10 = driver.find_element_by_xpath('//*[@id="whenStartInput"]/input').send_keys('asap')
element11 = driver.find_element_by_xpath('//*[@id="address"]').send_keys('Panchkula')
element12 = driver.find_element_by_xpath('//*[@id="resume"]').send_keys('C:/Users/Arjun Sharma/Downloads/Arjun_Sharma_-_Sr._Software_Test_Engineer_.pdf')
element13 = driver.find_element_by_xpath('//*[@id="yes"]').click()
element14 = driver.find_element_by_xpath('//form/button[1]').click()
# Testcase 4 and 5
# create a database connection
try:
    db = MySQLdb.connect("localhost", "userName", "Password", "DB_Name")
    # define a cursor object
    cursor = db.cursor
    # query
    sql = "SELECT * from tb_employee where firstname='Arjun'"
    # execute query
    result = cursor.execute(sql)
    # fetching all the data from the db
    while result.next():
        first_name = result.get("firstName")
        last_name = result.get("lastName")
        email = result.get("email")
        current_company = result.get("currentCompany")
        mobile_no = result.get("phone")
        DOB = result.get("dateOfBirth")
        apply_position = result.get("applyPos")
        portfolio = result.get("portFolio")
        sal_req = result.get("salReq")
        start_period = result.get("startTime")
        address = result.get("address")
        resume = result.get("resume")
        relocate = result.get("is_relocate")
        # assuming 0- yes, 1- no
        email_triggered = result.get("email_sent")
    # fetching value of the email. 0- email sent, 1- email not sent

except (MySQLdb.Error, MySQLdb.Warning) as s:
    print(s, 'Error while entering db')

    try:
    # verification of data entered using assertion
        assert first_name == 'Arjun', 'first_name is equal to Arjun'
        assert last_name == 'Sharma', 'last_name is equal to Sharma'
        assert email == 'sharmaarjun2850@gmail.com',\
            'email is equal to sharmaarjun2850@gmail.com'
        assert current_company == 'clicklabs', 'current_company is equal to clicklabs'
        assert mobile_no == '9855579616', 'phone is equal to 9855579616'
        assert DOB == '1993-07-18', 'DOB is equal to 18July 1993'
        assert apply_position == 'Sr SDET', 'position applied for is equal to Sr SDET'
        assert portfolio == 'https://www.linkedin.com/in/arjun-sharma-1b6ba3a7/',\
            'portfolio is equal to linkedIN link'
        assert sal_req == '12lpa', 'sal_req is equal to 12lpa'
        assert start_period == 'asap', 'start_period is equal to asap'
        assert address == 'panchkula', 'address is equal to panchkula'
        assert resume == 'resume link', 'resume is equal to resume link'
        assert relocate == 0, 'relocate is equal to 0'
        assert email_triggered == 0, 'email_triggered is equal to 0'
        # close object
        cursor.close()
        # close connection
        db.close()
    except Exception:
        print(traceback.format_exc())

driver.quit()