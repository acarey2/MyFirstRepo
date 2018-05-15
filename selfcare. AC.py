import pyautogui as pg
import webbrowser
import time

#selfcare
#findingyourself

answer= pg.prompt("""
which do you want to enhance
a. skin
b. makeup look
c. confidence
""")

if answer == "a":
    skintype= pg.prompt("""skin type?
a. dry
b. sensitive
c. combination
d. oily
""")
    if skintype== "a":

        webbrowser.open("https://www.sephora.com/product/rainforest-the-sea-deep-dive-cleansing-gel-P405096?keyword=tarte%20deep%20dive")
        webbrowser.open("https://www.sephora.com/product/tsubaki-swirl-two-part-gel-cream-deep-hydration-moisturizer-P415943")
        webbrowser.open("https://www.sephora.com/product/water-sleeping-mask-P420651?skuId=1966241&icid2=laneige_lp_bestsellers_carousel_us:p420651")

    if skintype== "b":
        webbrowser.open("https://www.sephora.com/product/ceramidin-skin-friendly-nanoskin-sheet-mask-P409349?skuId=1826346&icid2=products%20grid:p409349")
        webbrowser.open("https://www.sephora.com/product/natural-moisturizing-factors-ha-P427414?keyword=the%20ordinary%20natural")
        webbbrower.open("https://www.sephora.com/product/rise-shine-gentle-cleanser-P428249?skuId=2048841&icid2=products%20grid:p428249")
    if skintype== "c":
        webbrowser.open("https://www.sephora.com/product/the-true-cream-aqua-bomb-P394639?skuId=1686427&icid2=products%20grid:p394639")
        webbrowser.open("https://www.sephora.com/product/soy-face-cleanser-P7880?skuId=487694&icid2=products%20grid:p7880")
        webbrowser.open("https://www.sephora.com/product/watermelon-glow-sleeping-mask-P420160")
    if skintype== "d":
        webbrowser.open("https://www.sephora.com/product/acne-clearing-wash-P410883")
        webbrowser.open("https://www.sephora.com/product/counter-balance-mattifying-moisture-creme-P42345?icid2=similar%20products:p42345:product")
        webbrowser.open("https://www.sephora.com/product/clear-improvement-active-charcoal-mask-to-clear-pores-P297524?skuId=1375773&icid2=products%20grid:p297524")
    
    

elif answer == "b":
   makeup= pg.prompt("""what type of makeup look?
a. natural
b. night out
c. glowy
d. bold
""")
   if makeup=="a":
       webbrowser.open("https://www.sephora.com/product/natural-eyes-eyeshadow-palette-P429602?skuId=2064483&icid2=products%20grid:p429602")
       webbrowser.open("https://www.sephora.com/product/tinted-brow-gel-P187202?skuId=998872&icid2=products%20grid:p187202")
       webbrowser.open("https://www.sephora.com/product/highlighter-P404798?keyword=milk%20highlighter")
   if makeup=="b":
       webbrowser.open("https://www.sephora.com/product/all-nighter-long-lasting-makeup-setting-spray-P263504")
       webbrowser.open("https://www.sephora.com/product/buxom-lash-mascara-P228204?skuId=1143486&icid2=products%20grid:p228204")
       webbrowser.open("https://www.sephora.com/product/park-ave-princess-contour-palette-P426314?skuId=2027795&icid2=products%20grid:p426314")
       
   if makeup=="c":
       webbrowser.open("https://www.sephora.com/product/custom-enhancer-drops-P409765?skuId=1826940&icid2=products%20grid:p409765")
       webbrowser.open("https://www.sephora.com/product/killawatt-freestyle-highlighter-P64879845?icid2=:p64879845:product")
       webbrowser.open("https://www.sephora.com/product/rainforest-the-sea-water-foundation-broad-spectrum-spf-15-P405102?skuId=1900794&icid2=products%20grid:p405102")
   if makeup=="d":
       webbrowser.open("https://www.sephora.com/product/tropic-palette-P429004?keyword=tropic%20eyeshadow")
       webbrowser.open("https://www.sephora.com/product/glitter-pop-peel-off-eyeliner-P425200?skuId=1994375&icid2=products%20grid:p425200")
       webbrowser.open("https://www.sephora.com/product/mermaid-sea-quins-be-mermaid-make-waves-collection-P429963")

       
elif answer == "c":
    confidence= pg.prompt(""" what quality about yourself would you like to elevate
a. confidence
b. self love
c. happiness
""")
    if confidence=="a":
       webbrowser.open("https://zenhabits.net/25-killer-actions-to-boost-your-self-confidence/")
       webbrowser.open("https://www.youtube.com/watch?v=l_NYrWqUR40")

    if confidence=="b":
       webbrowser.open("https://www.teenvogue.com/gallery/free-self-care-gift-guide")
       webbrowser.open("https://tinybuddha.com/blog/21-tips-to-release-self-neglect-and-love-yourself-in-action/")

    if confidence=="c":
       webbrowser.open("https://www.positivityblog.com/")
       webbrowser.open("https://www.realsimple.com/health/mind-mood/emotional-health/10-ways-happier")
   
       




       


