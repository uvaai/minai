
## Normal equation bug

De update voor de meest recente versie van *scikit-learn* heeft de implementatie van
`LinearRegression()` behoorlijk aangepast, waardoor deze niet altijd meer normal equation gebruikt
voor de oplossing van $$\mathb{\hat{w}}, \hat{b}$$. De reden hiervoor is niet heel belangrijk, maar
het zorgt er helaas wel voor dat de resultaten van de module 5 notebook die gebruik maken van de
functie `normal_fix(X, y)` niet altijd correct waren voor jullie.

Hieronder dus een belangrijke recificatie voor die module, die hopelijk ook helpt om een beter
visueel beeld te krijgen van wat overfitting precies is:

### Assignment 10: Plotting the Normal fit

Hier zit het grootste verschil, want de polynomial van degree 30 zou altijd *heel sterk* moeten
overfitten. De degree daar is namelijk net zo groot als het totale aantal datapunten, dus het
model zou hier veel te flexibel moeten zijn. Het resultaat zou er eigenlijk zoals hieronder uit
horen te zien

![Overfitted polynomial function of degree 30](overfit1.png)

Gegeven deze nieuwe plot, is het volgende stukje tekst uit de opdracht ook een stuk logischer

> Increasing the degree of the polynomial will always add more parameters to the model, as the
> dimensions of $$\mathbf{w}$$ must also increase. More parameters means the model is more
> "flexible", as there are more values to change and create the *perfect fit*. This means, as
> you increase the degree of the model, the cost on the training data will always decrease, and
> the confidence bounds will always move closer together.
> 
> So, is the perfect model just when the line moves exactly through all the data points and the
> confidence bounds are completely on top of the fitted line? No, because of the noise in the
> data, perfectly fitting all the data points will probably not generalize very well to new
> points. **You can actually see a clear example of this in the degree 30 polynomial plot above.
> Between the first and second point, and between the last point and the point before that, the
> function makes strange spikes, that don't correspond to any data point. This is the best way for
> the polynomial to exactly fit these specific points apparently, but it doesn't capture any part
> of the underlying trend *between* these two points.**
> 
> This type of model is said to be overfitting. It is fitting the noise in the data and no longer
> approximating the true function $g$. _You can detect overfitting by testing with data points you
> didn't train on._

### Assignment 12: Model selection

Hier is het verschil wat minder groot, maar in de plot met *Underfitting vs. Overfitting* zou je
een grotere gemiddelde validatie kost verwachten voor de hogere degrees, zoals hieronder

![Underfitting vs. Overfitting with normal equation](overfit2.png)

De plot hierboven zit nu dus ook heel dicht bij wat je theoretisch zou verwachten voor de
vergelijking van de training en validatie kosten van verschillende versies van een model. De plot
laat nu precies zien welke degrees een underfit opleveren, welke degrees een overfit opleveren, en
welke degrees een goed model maken dat ook generaliseert naar de validatie data. Dit goed kunnen
herkennen is erg nuttig voor heel veel verschillende machine learning modellen, niet alleen
polynomial regression.

### Optioneel: Verbeterde code

Mocht je zelf willen experimenteren met de verbeterde Normal equation, dan kun je de definitie van
`normal_fix(X, y)` in de notebook vervangen met de nieuwe `linalg` implementatie hieronder

    from scipy.linalg import lstsq

    def normal_fit(X, y):
        DX = np.hstack((np.ones(y.shape), X))
        DW = lstsq(DX, y)
        
        return DW[0][1:], DW[0][0,0]

Deze versie heeft geen comments, want wat deze implementatie precies doet, is misschien wat meer
detail dan nodig. Mocht je wel nog interesse hebben in de werking hiervan, dan kun je hier
natuurlijk altijd nog in de les naar vragen.


