

def setting_fun(filename='setting',**details):
    if details:
        with open('setting.abcd','w') as file:
            for k,v in details.items():
                file.write(f'{k}->{v}')

setting_fun(color='blue',alpha= 1 , gamma=2,filename='color_setting.txt')

setting_fun(window='xp',ram= '16gb' , wallpaer='powerbank',
              filename='pc_setting.txt')
