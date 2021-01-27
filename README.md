# Py_term_color_check
A demonstration of the diffrent possibilites to printing colored text to a terminal in the python language.

För att enkelt få färg och bakgrundsfärg i terminalen så är det smidigt att använda sig av ANSI escape character sequence koder. Dessa är koder som man i kombination med en stdout IO call i en terminal ändrar färger på såväl bakgrund som text i några basic nyanser. 

ANSI funger klockrent i Unix/Macs, men i win32 är det inte by default enablat, samt funkar lite annorlunda. Detta går att lösa genom att använda sig av ett Python paket som kallas Colorama. Det kommer medinstallerat de senare versionerna av python och förutom att det ger en enkelt sätt att garantera funktionalitet över Unix/Mac och Windows, så ger det också ett interface som gör det lite enklare istället för att jobba med dem rena koderna.

Filen colors.py Innehåller en prototyp implementation av hur detta skulle kunna se ut i relation till vårt specifika projekt.