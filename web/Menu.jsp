<%-- 
    Document   : Menu
    Created on : Sep 8, 2017, 12:08:14 AM
    Author     : estre
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import = "Menu.Crear"%>
<%@page import = "Menu.Descargar"%>
<!DOCTYPE html>
<html>
    <!-- Scripts-->
   <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <link rel="apple-touch-icon" href="apple-touch-icon.png">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        
        <!--For Plugins external css-->
        <link rel="stylesheet" href="css/plugins.css" />
        
        <!--Theme custom css -->
        <link rel="stylesheet" href="css/style.css"> <!-- Estilo de barra superior -->
        <!--Theme Responsive css-->
        <link rel="stylesheet" href="css/responsive.css" />
        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
        
        <script src="js/vendor/jquery-1.11.2.min.js"></script>
        <script src="js/vendor/bootstrap.min.js"></script>

        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
        
        <!-- text fonts -->
        <link rel="stylesheet" href="assets/css/ace-fonts.css" />
        <!-- ace styles -->
        <link rel="stylesheet" href="assets/css/ace.css" class="ace-main-stylesheet" id="main-ace-style" />
        <!-- ace settings handler -->
        <script src="assets/js/ace-extra.js"></script>

    </head>
   <body  data-spy="scroll" data-target="#main-navbar">
        <div class='preloader'><div class='loaded'>&nbsp;</div></div>
        <div id="menubar" class="main-menu">
             <nav class="navbar navbar-default navbar-fixed-top">
                <div class="container">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="navbar-header">
                        <h1><a href=""><B>USAC Driver</B></a></h1>                         
                    </div>
                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                       <ul class="nav navbar-nav navbar-right">
                          <li class="active"><a href="#crear">Crear<span class="sr-only">(current)</span></a></li>
                          <li><a href="#modificar">Modificar</a></li>
                          <li><a href="#eliminar">Eliminar</a></li>
                          <li><a href="#compartir">Compartir</a></li>
                          <li>
                             <a data-toggle="dropdown" href="#" class="dropdown-toggle">
                                <span class="user-info">
                                   <%= session.getAttribute("sesionusuario") %>
                                </span>
                                <i class="ace-icon fa fa-caret-down"></i>
                             </a>
                             <ul class="user-menu dropdown-menu-right dropdown-menu dropdown-yellow dropdown-caret dropdown-close">                               
                                <li><a href="Inicio.jsp">Salir &nbsp; <i class="fa fa-arrow-right fa-1x"></i></a></li>
                             </ul>
                          </li>                           
                       </ul>                         
                    </div><!-- /.navbar-collapse -->                    
                </div><!-- /.container-fluid -->
             </nav>        
        </div>     
        <header id="home" class="sections">
           <div class="row">
              <div class="homepage-style">
                 <div class="container">
                    <div class="col-md-12 col-sm-12 col-xs-12">
                        <div class="widget-box widget-color-green2">
                           <div class="widget-header">
                              <h4 class="widget-title lighter smaller">My Drive</h4>
                           </div>

                           <div class="widget-body">
                              <div class="widget-main padding-8">
                                 <ul class="collapsibleList">
                                    <li><button name="raizRoot" value="raizRoot">
                                          	<i class="fa fa-folder">raizRoot</i>
                                       </button>
                                       <ul>
                                          <div id="tabla"></div>
                                          <li>Child item</li>
                                          <li>Child item</li>
                                       </ul>
                                    </li>
                                 </ul>
                              </div>
                           </div>
                        </div>
                     </div>
                 </div>                                                                             
               </div>
            </div>
        </header>
        <section id="crear" class="sections">
         <div class="container">           
            <div class="row">
               <div class="heading">
                  <div class="title text-center arrow-right">
                     <h4 class="">Crear</h4>
                     <img class="hidden-xs" src="assets/images/right-arrow.png" alt="" />

                  </div>
               </div>
               <div class="portfolio-wrap">
                  <div class="portfolio">
                     <form method="post" action="crear" enctype="multipart/form-data">
                        <div class="col-md-6 col-sm-6 col-xs-12">
                           <div class="widget-box">
                              <div class="widget-header">
                                 <h4 class="widget-title">Cargar Archivo</h4>
                              </div>
                              <div class="widget-body">
                                 <div class="widget-main">                            
                                    <div class="form-group">
                                       <div class="col-xs-12">
                                          <input multiple="" type="file" name="multipleFile" id="id-input-file-3" />
                                          <!-- /section:custom/file-input -->
                                       </div>
                                    </div>
                                    <!-- #section:custom/file-input.filter -->
                                    <label>
                                       <button class="submit" >
                                          Subir Archivo
                                          <i class="ace-icon fa fa-arrow-right icon-on-right bigger-110"></i>
                                       </button>
                                    </label>                            
                                    <!-- /section:custom/file-input.filter -->
                                 </div>
                              </div>
                           </div>
                        </div>
                     </form>
                     <form method="post" action="descargar">
                        <div class="col-md-6 col-sm-6 col-xs-12">
                           <div class="widget-box">
                              <div class="widget-header">
                                 <h4 class="widget-title">Descargar Archivo</h4>
                              </div>
                              <div class="widget-body">
                                 <div class="widget-main">                            
                                    <div class="form-group">
                                       <div class="col-xs-12">
                                          <input class="form-control" type="text" id="descargaFile" name="descargaFile" placeholder="Nombre de Archivo">
                                       </div> 
                                       <label>
                                          <button class="submit">
                                             descargar
                                             <i class="ace-icon fa fa-arrow-right icon-on-right bigger-110"></i>
                                          </button>
                                       </label>   
                                    </div>
                                    <!-- #section:custom/file-input.filter -->
                                                            
                                    <!-- /section:custom/file-input.filter -->
                                 </div>
                              </div>
                           </div>
                        </div>                        
                     </form>                        
                     <form method="post" action="crearCarpeta">
                        <div class="col-md-6 col-sm-6 col-xs-12">
                           <div class="widget-box">
                              <div class="widget-header">
                                 <h4 class="widget-title">Crear Carpeta</h4>
                              </div>
                              <div class="widget-body">
                                 <div class="widget-main">                            
                                    <div class="form-group">
                                       <div class="col-xs-12">
                                          <input class="form-control" type="text" id="nombreCarpeta" name="nombreCarpeta" placeholder="Nombre de Archivo">
                                       </div> 
                                       <label>
                                          <button class="submit">
                                             Crear
                                             <i class="ace-icon fa fa-arrow-right icon-on-right bigger-110"></i>
                                          </button>
                                       </label>   
                                    </div>
                                    <!-- #section:custom/file-input.filter -->
                                                            
                                    <!-- /section:custom/file-input.filter -->
                                 </div>
                              </div>
                           </div>
                        </div>                        
                     </form>                        
                  </div>                  
               </div>               
            </div>
         </div>
        </section>
        <section id="modificar" class="sections">
           
        </section>
        <section id="eliminar" class="sections">
           
        </section>
        <section id="compartir" class="sections">
      <div class="scroll-top">

         <div class="scrollup">
            <i class="fa fa-angle-double-up"></i>
         </div>

      </div>  
    </body>
</html>


<script src="assets/js/jquery.autosize.js"></script>
<script src="assets/js/bootstrap-tag.js"></script>

<!-- ace scripts -->
<script src="assets/js/ace/elements.fileinput.js"></script>
<script src="assets/js/ace/ace.js"></script>
<script src="assets/js/ace/ace.widget-box.js"></script>
<script src="assets/js/fuelux/fuelux.tree.js"></script>
<script src="assets/js/ace/elements.treeview.js"></script>

<script type="text/javascript">
   jQuery(function($) {
      $('#id-input-file-3').ace_file_input({
              style:'well',
              btn_choose:'Click to choose',
              btn_change:null,
              no_icon:'ace-icon fa fa-cloud-upload',
              droppable:true,
              thumbnail:'small'
              ,
              preview_error : function(filename, error_code) {
                      //name of the file that failed
                      //error_code values
                      //1 = 'FILE_LOAD_FAILED',
                      //2 = 'IMAGE_LOAD_FAILED',
                      //3 = 'THUMBNAIL_FAILED'
                      //alert(error_code);
              }

      }).on('change', function(){
      });       
      
      $("button").click(function() {
            var nombreVar = $(this).val();
            $.post('ActionServlet', {
                  nombre : nombreVar,
            }, function(responseText) {
                  $('#tabla').html(responseText);
            });
        });
   });        
 
</script>