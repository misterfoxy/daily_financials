import smtplib


def email(close,change):
	html="""\
		<html>
			<head></head>
			<body>
				<h1>Daily Financials</h1>
				<p>Closing price of $""" + str(close) + """ for SPY, a change of """ +str(change)+"""!</p>		
			</body>
		</html>

	"""	
	return html
