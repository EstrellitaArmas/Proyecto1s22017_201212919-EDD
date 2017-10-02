package Menu;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Helpers.Conexion;
import Helpers.ParserJson;
import Helpers.CarpetasDTO;

@WebServlet(urlPatterns = {"/ActionServlet"})
public class ActionServlet extends HttpServlet {
	
	private static final long serialVersionUID = 1L;
	private ArrayList<Persona> personas = new ArrayList<>();

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType( "text/html; charset=iso-8859-1" );
		PrintWriter out = response.getWriter();
		
		// Obtengo los datos de la peticion
		String nombre = request.getParameter("nombre");
		String apellido = "apellido";
		String edad = "edad";
		
		if (!nombre.equals("") && !apellido.equals("") && !edad.equals("")) {
			// Creo el objeto persona y lo añado al arrayList
			Persona persona = new Persona(nombre, apellido, edad);
			personas.add(persona);
		}
                out.println("<ul class=\"collapsibleList\">");
		for(int i=0; i<personas.size(); i++){
			Persona persona = personas.get(i);
			out.println("<li><button name=\"raizRoot\" value=\"raizRoot\"><i class=\"fa fa-folder\">"+persona.getNombre()+"</i></button>");	
		}
		out.println("</ul>");
		
		
	}

}
