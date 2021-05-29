# class MyScreenManager(ScreenManager):
#     previous_screen = None

#     def set_screen(self, screen_name, side="left"):
#         self.previous_screen = {"name": self.current, "side": side}
#         self.transition.direction = side
#         self.current = screen_name

#     def goto_previous_screen(self):
#         self.set_screen(
#             self.previous_screen["name"],
#             side="right" if self.previous_screen["side"] == "left" else "left",
#         )

# def Smaller_Branchless(a):
#     ans= 1.0 * (a > 1.0) + 2.0 * (1.0 >= a)
#     return ans
# print(Smaller_Branchless(0.5))


# print(ord('a'),ord('A'))

# def numConcat(num1, num2):
# 	return num1 * (10 ** len(str(num2))) + num2


# print(numConcat(1,22))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from kivy.lang import Builder
# from kivy.base import runTouchApp

# KV = '''
# #:import DropShadow kivy.uix.effectwidget.DropShadowEffect
# <T@Label>:
#     size_hint_x: None
#     width: self.texture_size[0]
# <S@Slider>:
#     orientation: 'horizontal'
#     Label:
#         pos: root.pos
#         text: str(root.value)
# BoxLayout:
#     FloatLayout:
#         Widget:
#             bgr: bgr.value
#             bgb: bgb.value
#             bgg: bgg.value
#             bga: bga.value
#             canvas.before:
#                 Color:
#                     rgba: self.bgr or 0, self.bgg or 0, self.bgb or 0, self.bga or 0
#                 Rectangle:
#                     pos: self.pos
#                     size: self.size
#         EffectWidget:
#             id: effect
#             drop_shadow: DropShadow()
#             effects: [self.drop_shadow]
#             Label:
#                 text: ti.text
#                 font_size: font_size.value
#                 color: [r.value, g.value, b.value, a.value]
#     GridLayout:
#         cols: 2
#         T:
#             text: 'text'
#         TextInput:
#             id: ti
#             text: 'Test'
#         T:
#             text: 'font_size'
#         S:
#             id: font_size
#             min: 10
#             max: 500
#         T:
#             text: 'color_r'
#         S:
#             id: r
#             min: 0
#             max: 1
#         T:
#             text: 'color_g'
#         S:
#             id: g
#             min: 0
#             max: 1
#         T:
#             text: 'color_b'
#         S:
#             id: b
#             min: 0
#             max: 1
#         T:
#             text: 'color_a'
#         S:
#             id: a
#             min: 0
#             max: 1
#         T:
#             text: 'offset_x'
#         S:
#             min: -100
#             max: 100
#             step: 1
#             on_value: effect.drop_shadow.offset[0] = self.value
#         T:
#             text: 'offset_y'
#         S:
#             min: -100
#             max: 100
#             step: 1
#             on_value: effect.drop_shadow.offset[1] = self.value
#         T:
#             text: 'radius'
#         S:
#             min: 1
#             max: 10
#             on_value: effect.drop_shadow.radius = self.value
#         T:
#             text: 'sampling'
#         S:
#             min: 1
#             max: 10
#             on_value: effect.drop_shadow.sampling = self.value
#         T:
#             text: 'tint_r'
#         S:
#             min: 0
#             max: 1
#             on_value: effect.drop_shadow.tint[0] = self.value
#         T:
#             text: 'tint_g'
#         S:
#             min: 0
#             max: 1
#             on_value: effect.drop_shadow.tint[1] = self.value
#         T:
#             text: 'tint_b'
#         S:
#             min: 0
#             max: 1
#             on_value: effect.drop_shadow.tint[2] = self.value
#         T:
#             text: 'tint_a'
#         S:
#             min: 0
#             max: 1
#             on_value: effect.drop_shadow.tint[3] = self.value
#         T:
#             text: 'bgr'
#         S:
#             id: bgr
#             min: 0
#             max: 1
#         T:
#             text: 'bgg'
#         S:
#             id: bgg
#             min: 0
#             max: 1
#         T:
#             text: 'bgb'
#         S:
#             id: bgb
#             min: 0
#             max: 1
#         T:
#             text: 'bga'
#         S:
#             id: bga
#             min: 0
#             max: 1
# '''

# runTouchApp(Builder.load_string(KV))

# from traceback import print_exc
# try:
# 	1/0
# except Exception as e:
# 	print_exc()

# Python program to
# demonstrate private methods

# Creating a Base class
# class Base:

# 	# Declaring public method
# 	def fun(self):
# 		print("Public method")

# 	# Declaring private method
# 	def __fun(self):
# 		print("Private method")

# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):
		
# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
		
# 	def call_public(self):
		
# 		# Calling public method of base class
# 		print("\nInside derived class")
# 		self.fun()
		
# 	def call_private(self):
		
# 		# Calling private method of base class
# 		self.__fun()

# # Driver code
# obj1 = Base()

# # Calling public method
# obj1.fun()

# obj2 = Derived()
# obj2.call_public()

# # Uncommenting obj1.__fun() will
# # raise an AttributeError

# # Uncommenting obj2.call_private()
# # will also raise an AttributeError

# def test(a=None,b=None):
# 	if a:
# 		print(a)
# 	if b:
# 		print(b)

# test(a=1,b=2)

"""float sdCylinder(vec3 p, vec3 a, vec3 b, float r)
{
	vec3  ba = b - a;
	vec3  pa = p - a;
	float baba = dot(ba,ba);
	float paba = dot(pa,ba);
	float x = length(pa*baba-ba*paba) - r*baba;
	float y = abs(paba-baba*0.5)-baba*0.5;
	float x2 = x*x;
	float y2 = y*y*baba;
	
	float d = (max(x,y)<0.0)?-min(x2,y2):(((x>0.0)?x2:0.0)+((y>0.0)?y2:0.0));
	
	return sign(d)*sqrt(abs(d))/baba;
}

float map( in vec3 pos )
{
	return sdCylinder(pos, vec3(0.0,-0.025,-0.0), vec3(0.02,0.025,0.005), 0.1 );
}

// http://iquilezles.org/www/articles/normalsSDF/normalsSDF.htm
vec3 calcNormal( in vec3 pos )
{
	vec2 e = vec2(1.0,-1.0)*0.5773;
	const float eps = 0.0005;
	return normalize( e.xyy*map( pos + e.xyy*eps ) + 
					  e.yyx*map( pos + e.yyx*eps ) + 
					  e.yxy*map( pos + e.yxy*eps ) + 
					  e.xxx*map( pos + e.xxx*eps ) );
}
	
#define AA 3

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	 // camera movement 
	float an = 0.0;
	vec3 ro = vec3( 1.0*cos(an), 0.4, 1.0*sin(an) );
	vec3 ta = vec3( 0.0, 0.0, 0.0 );
	// camera matrix
	vec3 ww = normalize( ta - ro );
	vec3 uu = normalize( cross(ww,vec3(0.0,1.0,0.0) ) );
	vec3 vv = normalize( cross(uu,ww));

		
	vec3 tot = vec3(0.0);
	
	#if AA>1
	for( int m=0; m<AA; m++ )
	for( int n=0; n<AA; n++ )
	{
		// pixel coordinates
		vec2 o = vec2(float(m),float(n)) / float(AA) - 0.5;
		vec2 p = (-iResolution.xy + 2.0*(fragCoord+o))/iResolution.y;
		#else    
		vec2 p = (-iResolution.xy + 2.0*fragCoord)/iResolution.y;
		#endif

		// create view ray
		vec3 rd = normalize( p.x*uu + p.y*vv + 1.5*ww );

		// raymarch
		const float tmax = 3.0;
		float t = 0.0;
		for( int i=0; i<256; i++ )
		{
			vec3 pos = ro + t*rd;
			float h = map(pos);
			if( h<0.0001 || t>tmax ) break;
			t += h;
		}
		
	
		// shading/lighting 
		vec3 col = vec3(0.0);
		if( t<tmax )
		{
			vec3 pos = ro + t*rd;
			vec3 nor = calcNormal(pos);
			float dif = clamp( dot(nor,vec3(0.57703)), 0.0, 1.0 );
			float amb = 0.5 + 0.5*dot(nor,vec3(0.0,1.0,0.0));
			col = vec3(0.2,0.3,0.4)*amb + vec3(0.8,0.7,0.5)*dif;
		}

		// gamma        
		col = sqrt( col );
		tot += col;
	#if AA>1
	}
	tot /= float(AA*AA);
	#endif

	fragColor = vec4( tot, 1.0 );
}
"""
# import sqlite3

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d

# con = sqlite3.connect(":memory:")
# con.row_factory = dict_factory
# cur = con.cursor()
# cur.execute("select 1 as b")
# print(cur.fetchone()["b"])

# con.close()



# import inspectshow
# print(dir(inspectshow))
# show = inspectshow.showtree()

# # inspectshow for given module/package
# show("kivymd")

# from kivy.storage.jsonstore import JsonStore

# store = JsonStore('hello.json')

# # put some values
# store.put('tito', name='Mathieu', org='kivy')
# store.put('tshirtman', name='Gabriel', age=27)

# # using the same index key erases all previously added key-value pairs
# store.put('tito', name='Mathieu', age=30)

# # get a value using a index key and key
# print('tito is', store.get('tito')['age'])

# # or guess the key/entry for a part of the key
# for item in store.find(name='Gabriel'):
#     print('tshirtmans index key is', item[0])
#     print('his key value pairs are', str(item[1]))

# from kivy.storage.jsonstore import JsonStore

# store = JsonStore('hello.json')
# if store.exists('tito'):
#     print('tite exists:', store.get('tito'))
#     store.delete('tito')

# a = "Madhavaram"

# print(a.find("a"))

# def findAll(s,t):
#     """returns all indices where substring t occurs in string s"""
#     indices = []
#     i = s.find(t)
#     while i > -1:
#         indices.append(i)
#         i = s.find(t,i+1)
#     return indices

# print(findAll(a,"Ma"))

# def before_and_after(value, a):
# 	pos_a = value.find(a)
# 	if pos_a == -1: return None
# 	adjusted_pos_ = pos_a + len(a)
# 	return [value[0:pos_a] , value[adjusted_pos_:]]


# test = "Tryi2ying"

# print(before_and_after(test,'yi'))


# from setuptools import find_packages

# print(find_packages())


##Threading Example
# import time
# from kivy.app import App
# from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
# import threading
# from kivy.lang.builder import Builder
# KV = """
# BoxLayout:
#     Button:
#         text: 'Run Thread' if app.thread is None else 'Cancel Thread'
#         on_press: app.toggle_thread()
#     Label:
#         canvas.before:
#             Color:
#                 rgba: 1, 1, 1, 0.5
#             Rectangle:
#                 pos: self.pos
#                 size: self.size[0] * (app.thread_percent / 100), self.size[1]
#         text: 'Thread Percent: '+str(app.thread_percent) if app.thread else 'Thread Stopped'
# """

# class Test(App):
#     canceling_thread = BooleanProperty(False)
#     thread = ObjectProperty(allownone=True)
#     thread_percent = NumericProperty(0)

#     def build(self):
#         return Builder.load_string(KV)

#     def toggle_thread(self):
#         if self.thread is not None:  #Thread is already running, cancel it
#             self.canceling_thread = True
#             return
#         self.canceling_thread = False
#         self.thread_percent = 0
#         self.thread = threading.Thread(target=self.thread_function)
#         self.thread.start()

#     def thread_function(self):
#         while not self.canceling_thread:  #This is the main loop for the thread
#             self.thread_percent += 1
#             time.sleep(.2)  #Placeholder, actual processing would be done here
#             if self.thread_percent == 100:  #Check if processing is done
#                 break
#         self.thread = None  #Cleanup after thread loop is done

#     def on_stop(self):
#         self.canceling_thread = True
#         while self.thread is not None:  #Wait for thread to stop so kivy won't crash
#             time.sleep(0.01)

# Test().run()