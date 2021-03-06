<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="refresh" content="0.01"/>

    <title>Sudoku</title>
    <!-- Styles -->
    <link href="/css/reset.css" rel="stylesheet">
    <link href="/css/style.css" rel="stylesheet">
    <link href="/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
      <section class="center pad-mar">
        <h1 class="text-center">Solving a Sudoku</h1>
    </section>
    <section class="container center">
        <table class="text-center ml-auto mr-auto">
            <tr>
                <td class="cell c{{c00}}">{{c00}}</td>
                <td class="cell c{{c01}}">{{c01}}</td>
                <td class="cell c{{c02}}">{{c02}}</td>
                <td class="cell c{{c03}}">{{c03}}</td>
                <td class="cell c{{c04}}">{{c04}}</td>
                <td class="cell c{{c05}}">{{c05}}</td>
                <td class="cell c{{c06}}">{{c06}}</td>
                <td class="cell c{{c07}}">{{c07}}</td>
                <td class="cell c{{c08}}">{{c08}}</td>
            </tr>
            <tr>
                <td class="cell c{{c10}}">{{c10}}</td>
                <td class="cell c{{c11}}">{{c11}}</td>
                <td class="cell c{{c12}}">{{c12}}</td>
                <td class="cell c{{c13}}">{{c13}}</td>
                <td class="cell c{{c14}}">{{c14}}</td>
                <td class="cell c{{c15}}">{{c15}}</td>
                <td class="cell c{{c16}}">{{c16}}</td>
                <td class="cell c{{c17}}">{{c17}}</td>
                <td class="cell c{{c18}}">{{c18}}</td>
            </tr>
            <tr>
                <td class="cell c{{c20}}">{{c20}}</td>
                <td class="cell c{{c21}}">{{c21}}</td>
                <td class="cell c{{c22}}">{{c22}}</td>
                <td class="cell c{{c23}}">{{c23}}</td>
                <td class="cell c{{c24}}">{{c24}}</td>
                <td class="cell c{{c25}}">{{c25}}</td>
                <td class="cell c{{c26}}">{{c26}}</td>
                <td class="cell c{{c27}}">{{c27}}</td>
                <td class="cell c{{c28}}">{{c28}}</td>
            </tr>
            <tr>
                <td class="cell c{{c30}}">{{c30}}</td>
                <td class="cell c{{c31}}">{{c31}}</td>
                <td class="cell c{{c32}}">{{c32}}</td>
                <td class="cell c{{c33}}">{{c33}}</td>
                <td class="cell c{{c34}}">{{c34}}</td>
                <td class="cell c{{c35}}">{{c35}}</td>
                <td class="cell c{{c36}}">{{c36}}</td>
                <td class="cell c{{c37}}">{{c37}}</td>
                <td class="cell c{{c38}}">{{c38}}</td>
            </tr>
            <tr>
                <td class="cell c{{c40}}">{{c40}}</td>
                <td class="cell c{{c41}}">{{c41}}</td>
                <td class="cell c{{c42}}">{{c42}}</td>
                <td class="cell c{{c43}}">{{c43}}</td>
                <td class="cell c{{c44}}">{{c44}}</td>
                <td class="cell c{{c45}}">{{c45}}</td>
                <td class="cell c{{c46}}">{{c46}}</td>
                <td class="cell c{{c47}}">{{c47}}</td>
                <td class="cell c{{c48}}">{{c48}}</td>
            </tr>
            <tr>
                <td class="cell c{{c50}}">{{c50}}</td>
                <td class="cell c{{c51}}">{{c51}}</td>
                <td class="cell c{{c52}}">{{c52}}</td>
                <td class="cell c{{c53}}">{{c53}}</td>
                <td class="cell c{{c54}}">{{c54}}</td>
                <td class="cell c{{c55}}">{{c55}}</td>
                <td class="cell c{{c56}}">{{c56}}</td>
                <td class="cell c{{c57}}">{{c57}}</td>
                <td class="cell c{{c58}}">{{c58}}</td>
            </tr>
            <tr>
                <td class="cell c{{c60}}">{{c60}}</td>
                <td class="cell c{{c61}}">{{c61}}</td>
                <td class="cell c{{c62}}">{{c62}}</td>
                <td class="cell c{{c63}}">{{c63}}</td>
                <td class="cell c{{c64}}">{{c64}}</td>
                <td class="cell c{{c65}}">{{c65}}</td>
                <td class="cell c{{c66}}">{{c66}}</td>
                <td class="cell c{{c67}}">{{c67}}</td>
                <td class="cell c{{c68}}">{{c68}}</td>
            </tr>
            <tr>
                <td class="cell c{{c70}}">{{c70}}</td>
                <td class="cell c{{c71}}">{{c71}}</td>
                <td class="cell c{{c72}}">{{c72}}</td>
                <td class="cell c{{c73}}">{{c73}}</td>
                <td class="cell c{{c74}}">{{c74}}</td>
                <td class="cell c{{c75}}">{{c75}}</td>
                <td class="cell c{{c76}}">{{c76}}</td>
                <td class="cell c{{c77}}">{{c77}}</td>
                <td class="cell c{{c78}}">{{c78}}</td>
            </tr>
            <tr>
                <td class="cell c{{c80}}">{{c80}}</td>
                <td class="cell c{{c81}}">{{c81}}</td>
                <td class="cell c{{c82}}">{{c82}}</td>
                <td class="cell c{{c83}}">{{c83}}</td>
                <td class="cell c{{c84}}">{{c84}}</td>
                <td class="cell c{{c85}}">{{c85}}</td>
                <td class="cell c{{c86}}">{{c86}}</td>
                <td class="cell c{{c87}}">{{c87}}</td>
                <td class="cell c{{c88}}">{{c88}}</td>
            </tr>
        </table>
    </section>

    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/jquery-3.2.1.slim.min.js"></script>
    <script src="/js/popper.min.js"></script>
    <script src="/js/slider.js"></script>
</body>

</html>