class Func:
	def __init__(self, to_exec):
		exec('self.f_x = lambda x, y: ' + to_exec)
	def __call__(self, x, y):
		return self.f_x(x, y)
