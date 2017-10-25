import pandas as pd
from matplotlib import pyplot as plt

# 使用os.getcwd()方法获取当前工作目录
#需要使用相对路径

data = pd.read_csv('Advertising.csv')
#print(data._values)
print(data[:4])


if __name__ == '__main__':
    x = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']

    #绘制
    plt.figure(figsize=(9,12))
    plt.subplot(311)
    plt.plot(data['TV'], y, 'ro')
    plt.grid()
    plt.subplot(312)
    plt.plot(data['Radio'], y, 'g^')
    plt.title('Radio')
    plt.grid()
    plt.subplot(313)
    plt.plot(data['Newspaper'], y, 'b*')
    plt.title('Newspaper')
    plt.grid()
    plt.tight_layout()
    plt.show()