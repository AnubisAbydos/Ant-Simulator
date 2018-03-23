import pygame
import Constants as const
import GroundTiles as ground
import TreeNode as tree
import UI as ui
import AntTrail as trail

class Attacker(Sprite):
	walkspeed = 0.025
	runspeed = 0.05
	hp0 = 3
	minicolor = 255, 255, 0
	size = 6
	attackrange = 1
	seerange = 6
	strength = 1
	shootable = False

	def __init__(self, *args, **kw):
		Sprite.__init__(self, *args, **kw)
		self.target = None
		self.path = None
		self.tractors = []

	def settarget(self, target):
		self.target = target
		self.waypoint = None

	def setpath(self, path):
		self.path = path
	
	def addtractor(self, tractor):
		if tractor not in self.tractors:
			self.tractors.append(tractor)
	
	def removetractor(self, tractor):
		if tractor in self.tractors:
			self.tractors.remove(tractor)

	def speedfactor(self):
		v = math.sqrt(self.vx**2 + self.vy**2)
		if v <= 0: return 1
		gx, gy = terrain.grad(self.x, self.y)
		d = (self.vx * gx + self.vy * gy) / v
		t = 0.5 if self.tractors else 1
		f = 2.0 if self.freerange else 1
		return min(max(1 - 0.12 * d, 0.4), 1) * t * f

	def approachtarget(self, scene):
		self.v = self.runspeed
		dx, dy = self.target.x - self.x, self.target.y - self.y
		if dx**2 + dy**2 < self.attackrange ** 2:
			self.vx, self.vy = 0, 0
			self.attack(self.target)
			return
		# choose the next place to walk to
		if not self.waypoint:
			dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
			dirs.sort(key = lambda d: -d[0]*dx - d[1]*dy)
			d0, d1 = dirs[0:2]
			a0, a1 = d0[0]*dx + d0[1]*dy, d1[0]*dx + d1[1]*dy
			# first choice of direction with probability a0/(a0+a1)
			fdir = d0 if random.random() * (a0 + a1) <= a0 else d1
			if self.cango(scene.empty_tile, self.x + fdir[0], self.y + fdir[1], self.target):
				self.waypoint = self.x + fdir[0], self.y + fdir[1]
			else:
				d0 = d0 if fdir == d1 else d1
				d1 = dirs[2]
				# second choice of direction with probability 5*a1/(a0+5*a1)
				fdir = d0 if random.random() * (a0 + 5 * a1) < 5 * a1 else d1
				if self.cango(scene.empty_tile, self.x + fdir[0], self.y + fdir[1], self.target):
					self.waypoint = self.x + fdir[0], self.y + fdir[1]
				else:
					fdir = d0 if fdir == d1 else d1
					self.waypoint = self.x + fdir[0], self.y + fdir[1]
		dx, dy = self.waypoint[0] - self.x, self.waypoint[1] - self.y
		if dx**2 + dy**2 < self.v**2:
			self.x, self.y = self.waypoint
			self.waypoint = None
		else:
			d = math.sqrt(dx**2 + dy**2)
			self.move(dx/d, dy/d)

	# attack the player if close enough, otherwise go in some random direction
	def wander(self, scene):
		if random.random() < 0.1:
			dx, dy = self.x - scene.player.x, self.y - scene.player.y
			if dx ** 2 + dy ** 2 < self.seerange ** 2:
				self.settarget(scene.player)
			else:
				self.v = self.walkspeed
				if self.vx or self.vy:
					self.move(0, 0)
				else:
					dx = 0.707 if random.random() < 0.5 else -0.707
					dy = 0.707 if random.random() < 0.5 else -0.707
					self.move(dx, dy)

	def update(self, scene):
		if self.target:
			self.approachtarget(scene)
		self.walk(scene.empty_tile, self.speedfactor())
		self.setheight()

	def attack(self, target):
		self.target.hurt(self.strength,self)
		self.alive = False

	def drawmini(self, surf, x0, y0):
		px, py = int((self.x - x0)//1), int((-self.y + y0)//1)
		surf.set_at((px, py), self.minicolor)

	def drawtractor(self, screen, looker=None):
		if not self.tractors: return
		looker = looker or camera
		x0, y0 = looker.screenpos(self.x, self.y, self.z + 3)
		w, h = 3+int(random.random() * 6), 3+int(random.random()*6)
		pygame.draw.rect(screen, effects.Tractor.color, (x0-w,y0-h,2*w,2*h))

