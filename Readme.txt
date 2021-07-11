Comandos definidos:
Auxilio: Sirve para una ayuda de comandos, y sugerencias
Amazon: Abre la página de Amazon
Google: Abre la página de Google
Google busca x: Busca en Google lo que le digas
    Google busca tilacino: Busca en Google la palabra tilacino
Youtube: Abre la página de Youtube
Youtube busca x: Busca en Youtube lo que le digas
    Youtube busca HolaSoyGerman: Busca en Youtube HolaSoyGerman
Facebook: Abre la página de Facebook
Telegram: Abre la página de Telegram
WhatsApp o What's Up: Abre la página de WhatsApp
Epic: Abre la aplicación de Epic Games
Netflix: Abre la página de Netflix
Netflix busca x: Busca en Netflix lo que le digas
    Netflix busca Rick and Morty: Busca en Netflix Rick and Morty
Programar o visual (el reconocedor de voz lo toma como diesel xD): Abre la aplicación de Visual Studio Code
Comando: abre la terminal de windows (cmd)
Tiempo: Te dice la hora actual
Fecha: Te dice la fecha actual
Traducir x: Traduce una frase de español a ingles
    Traducir Hola mundo: Hello World
Translate x: Traduce una frase de ingles a español
    Translate Hello World: Hola mundo


Para correr el programa es necesario tener python instalado, y en la terminal escribir
    python AsistenteVirtualJoranome.py
Y podrás ver lo que digas en la consola sin que esté en los comandos

Para hacerlo ejecutable .exe se necesita de este comando
    cxfreeze AsistenteVirtualJoranome.py --target-dir dist
Pero para hacerlo en 2o plano se ocupa este otro comando
    cxfreeze AsistenteVirtualJoranome.py --base-name=Win32GUI --target-dir dist
Luego se creará una carpeta con el nombre de "dist", entramos y ahí estará el ejecutable

Para ejecutarlo al encender nuestra PC, solo creamos un acceso directo del ejecutable y lo movemos a la carpeta de startup (la puedes abrir con Win+R y escribiendo shell:startup)


Para crear nuevos comandos es necesario saber cómo te lo reconoce el programa, di la palabra con el programa corriendo (con la terminal abierta, justo como se dijo en la linea 27)
Luego que tengas la palabra, después de la linea 105, y antes de la 108, colocas esto:
    if palabra in text:
Si quieres que abra un programa, defínela en las rutas como en la línea 14 y pon esta sintaxis (VariableRuta es como tu nombraste a la variable de la ruta)
    subprocess.call([VariableRuta])
Si quieres que abra una página solo pon
    webbrowser.open(VariablePagina)
Al ultimo pon la variable output con algo que identifiques a tu variable, esto sirve para que el asistente diga algo mientras hace lo que pediste
    output="Abriendo x"

Ejemplo
    Epic='C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
    if "Epic" in text:
        subprocess.call([Epic])
        output="Abriendo epic games"