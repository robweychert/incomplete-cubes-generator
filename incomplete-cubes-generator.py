# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

format = 'both' # 'svg', 'pdf', or 'both'
partial = 1 # draw all open cube variations with this many parts

# parts  variations
# -----------------
#   1 ......... 12
#   2 ......... 66
#   3 ........ 220
#   4 ........ 495
#   5 ........ 792
#   6 ........ 924
#   7 ........ 792
#   8 ........ 495
#   9 ........ 220
#  10 ......... 66
#  11 ......... 12

gl = 20 # grid lines
canvasWidth = 640 # ideally evenly divisible by gl
ar = 1.732 # axonometric ratio (x:1) (1.732:1 = isometric)

bgColor = (0, 0, 0)
widthColor = (0.66, 0.66, 0.66)
depthColor = (0.33, 0.33, 0.33)
topColor = (1, 1, 1)
gridColor = (0, 1, 1)

# ------------------------------------------------------------

# Define the axonometric grid according to the `gl`,
# `canvasWidth`, and `ar` settings above.

canvasHeight = canvasWidth / ar * 2
ygs = canvasHeight / gl # y axis grid segment
xgs = canvasWidth / gl # x axis grid segment

def bg(): # draw the background
    fill(*bgColor)
    rect(0, 0, canvasWidth, canvasHeight)

def grid(): # draw the axonometric grid
    stroke(*gridColor)
    for i in range(gl * 2):
        i *= ygs
        line(
            (0, 0 - canvasHeight + i),
            (canvasWidth, 0 - canvasHeight / 2 + i)
        )
        line(
            (0, canvasHeight * 2 - i),
            (canvasWidth, 0 + canvasHeight * 1.5 - i)
        )

# ------------------------------------------------------------

# The `block` function below creates a rendering of an
# extruded rectangle and places it on an axonometric grid
# determined by the `gl`, `canvasWidth`, and `ar` variables
# above. The width and depth planes are drawn to overlap with
# each other and the top plane to avoid an anti-aliased gap
# where the plane edges meet. The top plane is drawn true to 
# its form.

def block(x, y, width, depth, height):
    
    x *= xgs
    y *= ygs / 2
    width *= xgs
    height *= ygs
    depth *= xgs
    
    stroke(None)

    # Depth plane coordinates
    
    dx1 = x
    dy1 = y
    dx2 = x - width
    dy2 = y + width / ar + height
    dx3 = x + depth
    dy3 = y + depth / ar + height
    dx4 = dx3
    dy4 = y + depth / ar
    
    fill(*depthColor)
    
    if format == 'pdf' or format == 'both':
        polygon( (dx1, dy1), (dx2, dy2), (dx3, dy3), (dx4, dy4) )
    if format == 'svg' or format == 'both':    
        print('<polygon class="d" points="' + str(round(dx1)) + ' ' + str(round(canvasHeight - dy1, 2)) + ' ' + str(round(dx2)) + ' ' + str(round(canvasHeight - dy2, 2)) + ' ' + str(round(dx3)) + ' ' + str(round(canvasHeight - dy3, 2)) + ' ' + str(round(dx4)) + ' ' + str(round(canvasHeight - dy4, 2)) + '"/>')
    
    # Width plane coordinates
    
    wx1 = x
    wy1 = y
    wx2 = x - width
    wy2 = y + width / ar
    wx3 = wx2
    wy3 = y + width / ar + height
    wx4 = wx1
    wy4 = y + height + ygs / 2
    # wx5 = wx1
    # wy5 = y + height
    
    fill(*widthColor)
    
    if format == 'pdf' or format == 'both':
        polygon( (wx1, wy1), (wx2, wy2), (wx3, wy3), (wx4, wy4) )
    if format == 'svg' or format == 'both':    
        print('<polygon class="w" points="' + str(round(wx1)) + ' ' + str(round(canvasHeight - wy1, 2)) + ' ' + str(round(wx2)) + ' ' + str(round(canvasHeight - wy2, 2)) + ' ' + str(round(wx3)) + ' ' + str(round(canvasHeight - wy3, 2)) + ' ' + str(round(wx4)) + ' ' + str(round(canvasHeight - wy4, 2)) + '"/>')
    
    # Top plane coordinates
    
    tx1 = x
    ty1 = y + height
    tx2 = x - width
    ty2 = y + width / ar + height
    tx3 = x + depth - width
    ty3 = y + depth / ar + width / ar + height
    tx4 = x + depth
    ty4 = y + depth / ar + height
    
    fill(*topColor)

    if format == 'pdf' or format == 'both':
        polygon( (tx1, ty1), (tx2, ty2), (tx3, ty3), (tx4, ty4) )
    if format == 'svg' or format == 'both':    
        print('<polygon class="t" points="' + str(round(tx1)) + ' ' + str(round(canvasHeight - ty1, 2)) + ' ' + str(round(tx2)) + ' ' + str(round(canvasHeight - ty2, 2)) + ' ' + str(round(tx3)) + ' ' + str(round(canvasHeight - ty3, 2)) + ' ' + str(round(tx4)) + ' ' + str(round(canvasHeight - ty4, 2)) + '"/>')

# ------------------------------------------------------------

# The `parts` list below defines the `block` arguments for
# each of the 12 potential parts of an incomplete open cube.
# Additional alternate arguments are provided for some parts
# in the event that they overlap with adjacent parts in ways
# that disrupt the rendering's 3-D illusion.

parts = [
    ['part01', 17, 11, 8, 1, 1, 17, 11, 7, 1, 1], # bottom plane, top right
    ['part02', 10, 4, 1, 8, 1, 10, 4, 1, 7, 1], # bottom plane, bottom right
    ['part03', 10, 4, 8, 1, 1, 10, 4, 7, 1, 1], # bottom plane, bottom left
    ['part04', 3, 11, 1, 8, 1], # bottom plane, top left
    ['part05', 10, 18, 1, 1, 8, 10, 20, 1, 1, 7], # top post
    ['part06', 17, 11, 1, 1, 8], # right post
    ['part07', 10, 4, 1, 1, 8], # bottom post
    ['part08', 3, 11, 1, 1, 8], # left post
    ['part09', 17, 25, 8, 1, 1, 17, 25, 7, 1, 1], # top plane, top right
    ['part10', 10, 18, 1, 8, 1], # top plane, bottom right
    ['part11', 10, 18, 8, 1, 1], # top plane, bottom left
    ['part12', 3, 25, 1, 8, 1] # top plane, top left
]

# The parts above are listed in an orderly clockwise sequence,
# but to maintain the 3-D illusion, they need a specific
# stacking order.

stackingOrder = [
    'part04',
    'part08',
    'part05',
    'part12',
    'part09',
    'part01',
    'part06',
    'part02',
    'part03',
    'part07',
    'part10',
    'part11'
]

# Placeholder lists for unique combinations of parts:

u01 = [] #  1 part combos  (12)
u02 = [] #  2 part combos  (66)
u03 = [] #  3 part combos (220)
u04 = [] #  4 part combos (495)
u05 = [] #  5 part combos (792)
u06 = [] #  6 part combos (924)
u07 = [] #  7 part combos (792)
u08 = [] #  8 part combos (495)
u09 = [] #  9 part combos (220)
u10 = [] # 10 part combos  (66)
u11 = [] # 11 part combos  (12)
u12 = [] # 12 part combos   (1)

uniqueCombos = [ u01, u02, u03, u04, u05, u06, u07, u08, u09, u10, u11, u12 ]

# The `uniques` function below populates the placeholder lists
# above (`u01`, `u02`, etc), creating a directory of every
# possible unique combination of the 12 cube parts.

def uniques(numBase, numParts):
    currentCombo = []
    if numParts == u01:
        for part in parts:
            currentCombo.append(part)
            u01.append(currentCombo)
            currentCombo = []
    else:
        for combo in numBase:
            for part in parts:
                currentCombo = []
                for i in combo:
                    currentCombo.append(i)
                if part not in currentCombo:
                    currentCombo.append(part)
                    currentCombo.sort()
                    if currentCombo not in numParts:
                        numParts.append(currentCombo)

for i in range(len(uniqueCombos)):
    prev = i - 1
    uniques(uniqueCombos[prev], uniqueCombos[i])

# ------------------------------------------------------------

try:
    partial
except NameError: # if the `partial` variable isn't defined
    generate = 'full set' # draw ALL open cube variations (this can take quite awhile)
else:
    generate = 'partial set' # draw only open cube variations with the number of parts specified in `partial`

totalDrawings = 0

# The loop below puts everything together and generates the
# final images. For each combination in the `uniqueCombos`
# list, it draws the individual parts using the `block`
# function, taking stacking order into account, and drawing
# alternate versions of the parts when necessary. SVGs are
# printed to the console; PDFs are generated as external files
# in the same directory as this file and organized in sub-
# directories.

for comboSet in uniqueCombos:
    if generate == 'partial set' and uniqueCombos.index(comboSet) == partial - 1 or generate == 'full set':
        numDrawings = 0
        for combo in comboSet:
            if format == 'svg' or format == 'both':
                print('<div><svg viewbox="0 0 ' + str(canvasWidth) + ' ' + str(round(canvasHeight, 2)) + '">')
            numDrawings += 1
            totalDrawings += 1
            numParts = str(uniqueCombos.index(comboSet) + 1).zfill(2)
            if format == 'pdf' or format == 'both':
                destination = 'PDF/' + numParts + '/' + numParts + '-' + str(numDrawings).zfill(3) + '.pdf'
                newPage(canvasWidth, canvasHeight)
                bg()
            # grid()
            currentCombo = []
            for part in combo:
                currentCombo.append(part[0])
            for place in stackingOrder:
                for part in combo:
                    if part[0] == place:
                        if part[0] == 'part05' and 'part04' in currentCombo or part[0] == 'part01' and 'part04' in currentCombo or part[0] == 'part03' and 'part08' in currentCombo or part[0] == 'part01' and 'part05' in currentCombo or part[0] == 'part09' and 'part12' in currentCombo or part[0] == 'part02' and 'part06' in currentCombo:
                            block(part[6], part[7], part[8], part[9], part[10])
                        else:
                            block(part[1], part[2], part[3], part[4], part[5])
                        if format == 'pdf' or format == 'both':
                            import os
                            if not os.path.exists('PDF/' + numParts):
                                os.makedirs('PDF/' + numParts)
                            saveImage(destination, multipage=False)
            if format == 'svg' or format == 'both':
                print('</svg><p>' + str(partial) + '/' + str(numDrawings) + '</p></div>')

print('<!-- Total drawings generated: ' + str(totalDrawings) + ' -->')