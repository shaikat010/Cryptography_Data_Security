

<script src="https://www.desmos.com/api/v1.7/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>

<div id="calculator" style="width: 600px; height: 400px;"></div>


<script>
  var elt = document.getElementById('calculator');
  var calculator = Desmos.GraphingCalculator(elt);
  calculator.setExpression({ id: 'graph1', latex: 'y=x^2' });
</script>