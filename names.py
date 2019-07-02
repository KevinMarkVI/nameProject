
nameList = ['Amir','Amira','Asha','Assim','Azara','Azur','Azura','Bahram','Balthasar','Behrooz','Bibi','Bibiana','Caspar','Casper','Cy','Cyra','Cyrus','Dareh','Daria','Darice','Darioush','Darius','Darrius','Darya','Easter','Essie','Esther','Ettie','Farah','Farideh','Feroz','Gaspar','Gatha','Gazsi','Ghebers','Golnar','Greta','Gretchen','Gretel','Guebers','Hadassah','Hadassah','Hester','Hestia','Hetty','Ishtar','Jaleh','Jamsheed','Jasmine','Jasper','Jessamine','Jessamyn','Kansbar','Kaveh','Ksathra','Laila','Layla','Leila','Leilah','Lela','Leyla','Lila','Lilac','Madge','Maidie','Maisie','Majeed','Margaret','Margareta','Margaretta','Marjan','Marjorie','Mehrdad','Melchior','Meta','Minau','Mitra','Narda','Nasim','Parvaneh','Saeed','Said','Shabnan','Shahdi','Shahin','Shatrevar','Sholeh','Simin','Sohrab','Soray','Soroush','Soroushi','Taraneh','Vashti','Xenres','Yasmin','Zana','Zena','Zenda','Zuleika']

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

lastNames = ['berg','lohrasbpour','berg-lohrasbpour', 'lohrasbpour-berg', 'lohrasberg']

possibleEmails = []

def add(newName):
    for i in nameList:
        if newName == i:
            print(newName + ' is already in the list')
            return
    nameList.append(newName)

def createEmails(names, letters, surnames):
    for i in names:
        for j in letters:
            for k in surnames:
                possibleEmails.append(i +'.'+ j + '.' + k +"@gmail.com")
    print possibleEmails

createEmails(nameList, alphabet, lastNames)