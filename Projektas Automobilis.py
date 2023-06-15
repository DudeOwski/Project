import sqlite3

conn = sqlite3.connect('automobiliai.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS Automobilis (
        id INTEGER PRIMARY KEY,
        variklis TEXT,
        ratas TEXT,
        vairas TEXT,
        vairuotojas TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS Dalys (
        id INTEGER PRIMARY KEY,
        automobilio_id INTEGER,
        pavadinimas TEXT,
        patvarumas INTEGER,
        FOREIGN KEY (automobilio_id) REFERENCES Automobilis(id)
    )
''')

def sukurti_automobili(variklis, ratas, vairas, vairuotojas):
    c.execute('''
        INSERT INTO Automobilis (variklis, ratas, vairas, vairuotojas)
        VALUES (?, ?, ?, ?)
    ''', (variklis, ratas, vairas, vairuotojas))
    conn.commit()
    print("Automobilis sukurtas sėkmingai.")

def sukurti_dali(automobilio_id, pavadinimas, patvarumas):
    c.execute('''
        INSERT INTO Dalys (automobilio_id, pavadinimas, patvarumas)
        VALUES (?, ?, ?)
    ''', (automobilio_id, pavadinimas, patvarumas))
    conn.commit()
    print("Dalys sukurtos sėkmingai.")

def gauti_automobilius():
    c.execute('SELECT * FROM Automobilis')
    automobiliai = c.fetchall()
    for automobilis in automobiliai:
        print(automobilis)

def gauti_dalis(automobilio_id):
    c.execute('SELECT * FROM Dalys WHERE automobilio_id = ?', (automobilio_id,))
    dalys = c.fetchall()
    for daliu in dalys:
        print(daliu)

def atnaujinti_automobili(variklis, ratas, vairas, vairuotojas, automobilio_id):
    c.execute('''
        UPDATE Automobilis
        SET variklis = ?, ratas = ?, vairas = ?, vairuotojas = ?
        WHERE id = ?
    ''', (variklis, ratas, vairas, vairuotojas, automobilio_id))
    conn.commit()
    print("Automobilis atnaujintas sėkmingai.")

def atnaujinti_dali(pavadinimas, patvarumas, dalies_id):
    c.execute('''
        UPDATE Dalys
        SET pavadinimas = ?, patvarumas = ?
        WHERE id = ?
    ''', (pavadinimas, patvarumas, dalies_id))
    conn.commit()
    print("Dalys atnaujintos sėkmingai.")

def naikinti_automobili(automobilio_id):
    c.execute('DELETE FROM Automobilis WHERE id = ?', (automobilio_id,))
    conn.commit()
    print("Automobilis pašalintas sėkmingai.")

def naikinti_dali(dalies_id):
    c.execute('DELETE FROM Dalys WHERE id = ?', (dalies_id,))
    conn.commit()
    print("Dalys pašalintos sėkmingai.")

