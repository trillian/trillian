
model = Model()

for position in list_of_positions():
	data = getData(pos)
	
	mf = ModelFit()
	mf.model = model
	mf.data = data
	mf.fit()
	
	chain = mf.chain()
	
	value = mf.valueForParameter(parameter=aParameter)