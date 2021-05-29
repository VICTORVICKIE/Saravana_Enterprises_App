$HEADER$

uniform float t;
uniform float direction;

uniform vec2 resolution;
uniform sampler2D tex_in;
uniform sampler2D tex_out;

float progress;

vec4 getToColor(vec2 p){
	if(direction == 2.0){return texture2D(tex_in, p);}
	else{return texture2D(tex_out, p);}
}

vec4 getFromColor(vec2 p){
	if(direction == 2.0){return texture2D(tex_out, p);}
	else{return texture2D(tex_in, p);}
	
}

const vec4 black = vec4(0.0, 0.0, 0.0, 1.0);
const vec2 boundMin = vec2(0.0, 0.0);
const vec2 boundMax = vec2(1.0, 1.0);

bool inBounds (vec2 p) {
	return all(lessThan(boundMin, p)) && all(lessThan(p, boundMax));
}

vec4 transition (vec2 uv) {
	vec2 spfr,spto = vec2(-1.);
	float size = mix(1.0, 3.0, progress*0.2);
	spto = (uv + vec2(-0.5,-0.5))+vec2(0.5,0.5);
	spfr = (uv + vec2(0.0, 1.0 - progress));
	if(inBounds(spfr)){
		return getToColor(spfr);
	} else if(inBounds(spto)){
		return getFromColor(spto);
	}
}

void main( void ) {
	vec2  uv = gl_FragCoord.xy / resolution.xy;
	if(direction == 1.0){progress = 1.0 - t;}
	else{progress = t;}

	gl_FragColor = transition(uv);
}