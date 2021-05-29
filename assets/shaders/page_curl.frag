$HEADER$

#define pi 3.14159265359
#define radius .1

uniform float t;
uniform float direction;
uniform float aspect;
uniform vec2 resolution;
uniform sampler2D tex_in;
uniform sampler2D tex_out;

//IDK why but need to remap it to work, if something doesnt works try remap xD
float map(float value)
{
  float low_map_from = 0., high_map_from = 1., low_map_to = 0.075, high_map_to = -1.15;
  return low_map_to + (value - low_map_from) * (high_map_to - low_map_to) / (high_map_from - low_map_from);
}

void main( void )
{
    float aspect_ratio = 0.0;
    if (aspect == 1.0) {aspect_ratio = resolution.x / resolution.y;}
    else {aspect_ratio = resolution.y / resolution.x; }

    vec2 uv = gl_FragCoord.xy/resolution.xy;
    vec2 dir = vec2(0.15,-1.0);
    vec2 origin = vec2(0.0,0.0);
    
    float move = 0.;
    if (direction == 1.0) {move = map(t);}
    else {move = map(1.0 - t);}
    

    float proj = dot(uv - origin, dir);
    float dist = proj - move ;
    
    vec2 linePoint = uv - dist * dir ;
    
    if (dist > radius)
    {
        if (direction == 1.0) {gl_FragColor = texture2D(tex_in, uv);}
        else{gl_FragColor = texture2D(tex_out, uv);}

        gl_FragColor.rgb *= pow(clamp(dist - radius, 0., 1.) * 1.5, .2);
    }
    else if (dist >= 0.)
    {
        float theta = asin(dist / radius);
        vec2 p2 = linePoint + dir * (pi - theta) * radius;
        vec2 p1 = linePoint + dir * theta * radius;
        uv = (p2.x <= aspect_ratio && p2.y <= 1. && p2.x > 0. && p2.y > 0.) ? p2 : p1;

        if (direction == 1.0) {gl_FragColor = texture2D(tex_out, uv);}
        else {gl_FragColor = texture2D(tex_in, uv);}

        gl_FragColor.rgb *= pow(clamp((radius - dist) / radius, 0., 1.), .2);
    }
    else 
    {
        vec2 p = linePoint + dir * (abs(dist) + pi * radius) ;
        uv = (p.x <= aspect_ratio && p.y <= 1. && p.x > 0. && p.y > 0.) ? p : uv;
        
        if (direction == 1.0) {gl_FragColor = texture2D(tex_out, uv);}
        else {gl_FragColor = texture2D(tex_in, uv);}
    }
}