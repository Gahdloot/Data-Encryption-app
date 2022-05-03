import pandas as pd
import onetimepad


class Encore:
    # the Values to be passed here is the file data format
    def __init__(self, fname):

        ftype = ['csv', 'excel', 'txt']

        if fname in ftype:
            self.fname = fname
            pass
        else:
            raise AttributeError('The file type must be either csv, excel, txt')

    def dataframe(self, file):
        self.file = file
        df = pd.read_csv(file)
        self.df = df
        print(type(self.file))

    def lock_allAph(self, key):
        def bill(x, p=key):
            x = str(x)
            x = onetimepad.encrypt(x, p)
            return x

        for col in self.df.columns:
            self.df[col] = self.df[col].apply(bill)

        print(self.df)

    def unlock_allAph(self, key):
        def bill(x, p=key):
            x = str(x)
            x = onetimepad.decrypt(x, p)
            return x

        for col in self.df.columns:
            self.df[col] = self.df[col].apply(bill)

        print(self.df)

    def lockcol(self, key, col_name='Surname'):
        self.colname = col_name

        #print(self.df[self.colname])

        def bill(x, p=key):
            x = str(x)
            x = onetimepad.encrypt(x, p)
            return x

        self.df[self.colname] = self.df[self.colname].apply(bill)

        print(self.df[self.colname])

    def Unlockcol(self, key, col_name='Surname'):
        self.colname = col_name

        #print(self.df[self.colname])

        def bill(x, p=key):
            x = str(x)
            x = onetimepad.decrypt(x, p)
            return x

        self.df[self.colname] = self.df[self.colname].apply(bill)

        print(self.df[self.colname])

    def lock_row(self, key, row_num=1):
        self.row_num = row_num

        def bill(x, p=key):
            x = str(x)
            x = onetimepad.encrypt(x, p)
            return x

        self.df.iloc[self.row_num] = self.df.iloc[self.row_num].apply(bill)

        print(self.df)

    def unlock_row(self, key, row_num=1):
        self.row_num = row_num

        def bill(x, p=key):
            x = str(x)
            x = onetimepad.decrypt(x, p)
            return x

        self.df.iloc[self.row_num] = self.df.iloc[self.row_num].apply(bill)

        print(self.df)


    def lockrows(self, key, *args):
        self.args = args
        def bill(x, p=key):
            x = str(x)
            x = onetimepad.encrypt(x, p)
            return x

        for i in args:
            self.df.iloc[i] = self.df.iloc[i].apply(bill)

        print(self.df)

    def Unlockrows(self, key, *args):
        self.args = args
        def bill(x, p=key):
            x = str(x)
            x = onetimepad.decrypt(x, p)
            return x

        for i in args:
            self.df.iloc[i] = self.df.iloc[i].apply(bill)

        print(self.df)


    def lockcols(self, key, *args):
        self.args = args
        def bill(x, p=key):
            x = str(x)
            x = onetimepad.encrypt(x, p)
            return x

        for i in args:
            self.df.iloc[:,i] = self.df.iloc[:,i].apply(bill)

        print(self.df)

    def Unlockcols(self, key, *args):
        self.args = args
        def bill(x, p=key):
            x = str(x)
            x = onetimepad.decrypt(x, p)
            return x

        for i in args:
            self.df.iloc[:,i] = self.df.iloc[:,i].apply(bill)

    def __str__(self):
        return f'{self.df}'

    def save(self):
        if self.fname == 'csv':
            self.df.to_csv(self.file, index=False)
        elif self.fname == 'excel':
            self.df.to_excel(self.file, index=False)
        else:
            self.df.to_csv(self.file, index=False)




ecd = Encore('csv')
#
ecd.dataframe('data.csv')
ecd.lock_allAph('key')
#ecd.unlock_allAph()
#ecd.save()


