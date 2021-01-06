html = page_text
soup = BeautifulSoup( html , "html.parser" )
print(soup)

if test_url( soup ) :
        summary( soup )