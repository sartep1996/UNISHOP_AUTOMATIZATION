import win32com.client

ol = win32com.client.Dispatch('Outlook.Application')

olmailitem = 0x0 

newmail = ol.CreateItem(olmailitem)

newmail.Subject = 'Testing Mail'

newmail.To = 'vaidotas.levenauskas@unishop.lt'
newmail.CC = 'vaidotas.levenauskas@unishop.lt'
newmail.BCC = 'sandra.grokauskaite@unishop.lt'

newmail.Body= 'Hello, this is a test email to showcase how to send emails from Python and Outlook.'

attach = 'C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
newmail.Attachments.Add(attach)

newmail.Send()