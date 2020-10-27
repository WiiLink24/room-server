from room import app
@app.route('/url2/miiinfo.cgi')
def miiinfo():
    return '''
<MiiInfo>
    <code>0</code>
    <msg>thanks</msg>
</MiiInfo>'''
@app.route('/url2/related.cgi')
def related():
    # Hardcoded for now
    return '''
<RelatedMovies>
    <ver>399</ver>
    <leftmovieinfo>
        <rank>1</rank>
        <movieid>2</movieid>
        <title>Flight of a Shiba</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>2</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>3</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>4</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>5</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>6</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>7</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>8</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>9</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>10</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>11</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>12</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>13</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>14</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <leftmovieinfo>
        <rank>15</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </leftmovieinfo>
    <rightmovieinfo>
        <rank>1</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>2</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>3</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>4</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>5</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>6</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>7</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>8</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>9</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>10</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>11</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>12</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>13</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>14</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
    <rightmovieinfo>
        <rank>15</rank>
        <movieid>4</movieid>
        <title>Shiba the official</title>
    </rightmovieinfo>
</RelatedMovies>
'''
@app.route('/url2/evaluate.cgi',methods=['GET','POST'])
def evaluate():
    # TODO! Write mii to a database! 
    return '''
<Evaluate>
    <code>1</code>
    <msg>awesome thanks</msg>
</Evaluate>
'''
    
