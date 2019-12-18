# Python-Flask-Blog
Questo è l'esempio di un blog scritto in python utilizzando il framework flask.
Il progetto non è ancora ultimato. Appena ho tempo, lavoro permettendo, aggiornerò il codice. In questo momento comunque non è necessario che tutto funzioni ma piuttosto capire tutta la logica che c'è dietro poi a farlo funzionare per il meglio ci pensiamo durante la lezione, 
è probabile perciò che siano presenti dei bug. Per questo vi consiglio di iniziare con il vedere le seguenti cose:
* struttura generale del progetto, individuate tutti i moduli principali e cercate di capire i meccanismi che legano le varie parti.
Per intederci tutti i model utilizzati dai controller, come sono fatti questi model, le funzioni di estrazione dei dati e le strutture dei controller.
* Guardate se trovate parti che vi possono tornare utili per la vostra applicazione, ad esempio form html per l'immisiione dei dati, funzioni per l'archiviazione
, recupero dei dati tramite controller.
Per come è fatto ci sono spunti interessanti per i vostri progettini.

Se trovate dei bug e riuscite a risolverli siete entratti nell'ottica :) altrimente li vedremo assieme a lezione.


# Avviare il progetto
Per poter avviare il progetto dovete seguire i seguenti passi: 
* posizionarsi nella cartella del progetto in modo da poter creare il db
* eseguire i seguenti comandi in ordine:
    * `flask db init`
    * `flask db migrate`
    * `flask db upgrade`
    
 Adesso potete avviare l'applicazione eseguento il file `app.py`
