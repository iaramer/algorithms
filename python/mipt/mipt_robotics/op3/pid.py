#!/usr/bin/env python


class PID:

	def __init__(self, Kp, Ki=0.0, Kd=0.0, K_imax=30):
		self.K_p = Kp
		self.K_i = Ki
		self.K_d = Kd
		self.K_imax = K_imax
		self.p_error = 0.0
		self.i_error = 0.0
		self.d_error = 0.0


	def UpdateError(self, cte):
		cte = float(cte)
		self.d_error = cte - self.p_error
		self.p_error = cte
		self.i_error += cte
		if abs(self.i_error) > self.K_imax:
			self.i_error = self.K_imax
	
	def TotalError(self):
		return - self.K_p * self.p_error - self.K_i * self.i_error - self.K_d * self.d_error
