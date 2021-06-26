import sqlite3


class DB_helper:
    '''Сокращает рутинные операции с базами данных для упрощения
    понимания кода'''
    def __init__(self, db):
        self.con = sqlite3.connect(db)
    
    def select(self, table, item='*'):
        cur = self.con.cursor()
        return cur.execute(f'SELECT {item} FROM {table}').fetchall()
    
    def delete(self, table, condition):
        cur = self.con.cursor()
        cur.execute(f'''DELETE FROM {table} WHERE {condition}''')
        self.con.commit()
        cur.close()
    
    def insert(self, table, qnt, values):
        cur = self.con.cursor()
        unknown_values = ['?' for i in range(qnt)]
        cur.execute(f'''INSERT INTO {table} VALUES 
                    ({', '.join(unknown_values)})''', values)
        self.con.commit()
        cur.close()
    
    def update(self, table, value, condition):
        cur = self.con.cursor()
        cur.execute(f'UPDATE {table} SET {value} WHERE {condition}')
        self.con.commit()
        cur.close()
    
    def create(self, table, columns):
        cur = self.con.cursor()
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {table}({", ".join(columns)})''')
        self.con.commit()
        cur.close()
