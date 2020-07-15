# Build a dictionary containing the specified movie collection
library = {
              2005: [['Munich','Steven Spielberg']],
              2006: [['The Prestige','Christopher Nolan'],
                    ['The Departed','Martin Scorsese']],
              2007: [['Into the Wild', 'Sean Penn']],
              2008: [['The Dark Knight', 'Christopher Nolan']],
              2009: [['Mary and Max', 'Adam Elliot']],
              2010: [["The King's Speech",'Tom Hooper']],
              2011: [['The Artist', 'Michel Hazanavicius'],
                    ['The Help', 'Tate Taylor']],
              2012: [['Argo', 'Ben Affleck']],
              2013: [['12 Years a Slave', 'Steve McQueen']],
              2014: [['Birdman', 'Alejandro G. Inarritu']],
              2015: [['Spotlight', 'Tom McCarthy']],
              2016: [['The BFG', 'Steven Spielberg']]
              }


# Prompt the user for a year 
year = int(input("Enter a year between 2005 and 2016:\n"))
# Displaying the title(s) and directors(s) from that year
if(year<2005 or year>2016):
    print('N/A')
else:
    movies = library[year]
    for movie in movies:
        print(movie[0]+', '+movie[1])
print('')
# Display menu
option = ''
while option != 'q': # List of options to be carried out
    print('MENU')
    print('Sort by:')
    print('y - Year')
    print('d - Director')
    print('t - Movie title')
    print('q - Quit\n')
    option = input('Choose an option:\n')
    
# Display movies by year
    if(option == 'y'):
            for key in sorted(library.keys()):
                print(key,end=':')
                print('')
                for movie in library[key]:
                    print("\t"+movie[0]+", "+movie[1])
                print('')
                
# Display movies by director
    elif(option == 'd'):
            director_dict = {}
            for key in sorted(library.keys()):
                for movie in library[key]:
                    dire = movie[1]
                    if dire in director_dict:
                        director_dict[dire].append([movie[0],key])
                    else:
                        director_dict[dire] = [[movie[0],key]]

            for key in sorted(director_dict.keys()):
                print(key,end=':')
                print('')
                for dire in director_dict[key]:
                    print("\t"+ str(dire[0])+ ", "+str(dire[1]))
                print('')
                
#Display movies by movie title
    elif(option == 't'):
            title_dict = {}
            for key in sorted(library.keys()):
                for movie in library[key]:
                    title = movie[0]
                    if title in title_dict:
                        title_dict[title].append([movie[1],key])
                    else:
                        title_dict[title] = [[movie[1],key]]

            for key in sorted(title_dict.keys()):
                print(key,end=':')
                print('')
                for title in title_dict[key]:
                    print("\t"+str(title[0])+', '+str(title[1]))
                    print('')
    elif(option == 'q'):
        option = 'q'
    else:
        print('Invalid option')