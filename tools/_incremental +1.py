
size = 101
i = 1
if __name__ == '__main__':
  for x in range(size):
    i+=1
    print('<option value="%d">%d</option>'%i)
    print('send, ^t')
    print('sleep, 300')


'''
handle = driver.getWindowHandles();
print()
print('1 win name is ' + handle)
firstWinHandle = driver.getWindowHandle(); handle.remove(firstWinHandle);
winHandle=handle.iterator().next();
if (winHandle!=firstWinHandle):
    secondWinHandle = handle #Storing handle of second window handle
driver.switchTo().window(secondWinHandle);
'''


googleAccountIdentifier = driver.find_element_by_name('identifier')
googleAccountIdentifier.send_keys('drakeredwind01@gmail.com\n')

#input_txt.send_keys('operadriver\n')

#time.sleep(5) #see the result
#driver.quit()