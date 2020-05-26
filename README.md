# ottosoap

Python version
--------------

Le projet functionne avec Python 3.6 et 3.7

Installation:

1- Création venv:

    python3 -m venv ottosoap
    
2- Activation venv:

    source ottosoap/bin/activate
    
3- Installation requirements:

    pip install -r requirements.txt
    
4- Installation spyne:

    easy_install spyne==2.13.14b0
    
6- Appliquez une migration:

    python manage.py migrate
    
7- Démarrer le projet:

    python manage.py runserver
    
Tester le service:
1- Le service SOAP est disponible ci dessus: (Attention au slash à la fin.)

    http://localhost:8000/api/otto/
    
1- Postez ce message pour tester get_saisies: (Retorune toutes les saisies)

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope 
        xmlns:ns0="ottosoap.rhino"
        xmlns:ns2="rhino.views"
        xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <ns1:Body>
        <ns0:get_saisies>
        </ns0:get_saisies>
    </ns1:Body>
    </SOAP-ENV:Envelope>

2- Postez ce message pour tester get_saisie: (Retorune une saisie seulement)

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope 
       xmlns:ns0="otto.rhino"
       xmlns:ns2="rhino.views"
       xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
       xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
      <ns1:Body>
        <ns0:get_saisie>
          <ns0:pk>[id de la saisie]</ns0:pk>
        </ns0:get_saisie>
      </ns1:Body>
    </SOAP-ENV:Envelope>

1- Postez ce message pour tester le create_saisie: (Crée une saisie)

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope 
        xmlns:ns0="otto.rhino"
        xmlns:ns2="rhino.views"
        xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <ns1:Body>
        <ns0:create_saisie>
        <ns0:saisie>
            <ns2:route>kong</ns2:route>
            <ns2:application></ns2:application>
            <ns2:dtstart>2020-05-03T00:00:00</ns2:dtstart>
            <ns2:duree>1</ns2:duree>
            <ns2:cdret>10</ns2:cdret>
            <ns2:mois>mai</ns2:mois>
        </ns0:saisie>
        </ns0:create_saisie>
    </ns1:Body>
    </SOAP-ENV:Envelope>