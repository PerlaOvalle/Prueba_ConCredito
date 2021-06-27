from GooglePO import GooglePO

#Test1
googleTest = GooglePO()
googleTest.goToGoogle()
initialTitle = googleTest.getTitle()
googleTest.typeAndSearch('Perro')
resultsTitle = googleTest.getTitle()
assert initialTitle != resultsTitle

#Test2
googleTest.goToGoogle()
googleTest.typeAndSearch('San Bernardo', 'lucky')

#Test3
googleTest.goToGoogle()
googleTest.typeAndSearch('Boxer')
googleTest.typeAndSearch('Pastor Aleman', 'return')

#Test4
googleTest.goToGoogle()
googleTest.typeAndSearch('Pomerania')
resultStats = googleTest.getResultsStats()
googleTest.goToPage(2)
resultStatsPage2 = googleTest.getResultsStats()
assert resultStats != resultStatsPage2

#Test5
googleTest.goToGoogle()
googleTest.typeAndSearch('Labrador')
googleTest.goToImageSection()
googleTest.getFirstImage()
assert googleTest.getImagePreviewStatus() == True
googleTest.closeImagePreview()
assert googleTest.getImagePreviewStatus() == False

googleTest.close()



