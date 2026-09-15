#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(ggplot2)
library(caret)

# Load models
lda_LW  <- readRDS("lda_LW.rds")
lda_WT  <- readRDS("lda_WT.rds")
lda_LWT <- readRDS("lda_LWT.rds")


# User interface
ui <- fluidPage(
  
  titlePanel("Arrow vs Dart Projectile Point Classification"),
  
  sidebarLayout(
    
    sidebarPanel(
      
      numericInput("length", "Length (mm):",
                   value = NA, min = 0, step = 0.001),
      
      numericInput("width", "Width (mm):",
                   value = NA, min = 0, step = 0.001),
      
      numericInput("thickness", "Thickness (mm):",
                   value = NA, min = 0, step = 0.001)
      
    ),
    
    mainPanel(
      
      h3("Classification result"),
      
      #Text
      
      br(),
      
      h4("About the classification"),
      
      p("This application uses three Linear Discriminant Analysis (LDA) models trained to distinguish between arrow and dart projectile points. The models use different combinations of metric variables: Length + Width (LW), Width + Thickness (WT), and Length + Width + Thickness (LWT). The model used is automatically selected according to the variables entered. The application provides the estimated probability of membership in each category (Arrow or Dart). These probabilities represent the classification output and should be interpreted as estimates based on the trained models."),
      
      h4("Acerca de la clasificación"),
      
      p("Esta aplicación utiliza tres modelos de Análisis Discriminante Lineal (LDA), entrenados para distinguir entre puntas de flecha (Arrow) y puntas de dardo (Dart). Los modelos utilizan diferentes combinaciones de variables métricas: Length + Width (LW), Width + Thickness (WT) y Length + Width + Thickness (LWT). El modelo utilizado se selecciona automáticamente según las variables ingresadas. La aplicación proporciona la probabilidad estimada de pertenencia a cada categoría (Arrow o Dart). Estas probabilidades constituyen el resultado de la clasificación y deben interpretarse como una estimación basada en los modelos entrenados."),
      
      textOutput("model_used"),
      
      br(),
      
      textOutput("probability_arrow"),
      
      textOutput("probability_dart"),
      
      br(),
      
      plotOutput("probability_plot")
      
      
    )
  )
)


# Server
server <- function(input, output) {
  
  model_selected <- reactive({
    
    if (!is.na(input$length) &&
        !is.na(input$width) &&
        !is.na(input$thickness)) {
      
      lda_LWT
      
    } else if (!is.na(input$length) &&
               !is.na(input$width)) {
      
      lda_LW
      
    } else if (!is.na(input$width) &&
               !is.na(input$thickness)) {
      
      lda_WT
      
    } else {
      
      NULL
    }
  })
  
  
  model_name <- reactive({
    
    if (!is.na(input$length) &&
        !is.na(input$width) &&
        !is.na(input$thickness)) {
      
      "LWT (Length + Width + Thickness)"
      
    } else if (!is.na(input$length) &&
               !is.na(input$width)) {
      
      "LW (Length + Width)"
      
    } else if (!is.na(input$width) &&
               !is.na(input$thickness)) {
      
      "WT (Width + Thickness)"
      
    } else {
      
      "No model available"
    }
  })
  
  
  output$model_used <- renderText({
    
    paste("Model:", model_name())
    
  })
  
  
  output$probability_arrow <- renderText({
    
    model <- model_selected()
    
    if (is.null(model)) {
      return("Probability of arrow: —")
    }
    
    if (!is.na(input$length) &&
        !is.na(input$width) &&
        !is.na(input$thickness)) {
      
      newdata <- data.frame(
        length = input$length,
        width = input$width,
        thickness = input$thickness
      )
      
      print(newdata)
      
    } else if (!is.na(input$length) &&
               !is.na(input$width)) {
      
      newdata <- data.frame(
        length = input$length,
        width = input$width
      )
      
    } else if (!is.na(input$width) &&
               !is.na(input$thickness)) {
      
      newdata <- data.frame(
        width = input$width,
        thickness = input$thickness
      )
      
    }
    
    prob <- predict(model, newdata = newdata, type = "prob")
    
    paste0(
      "Probability of arrow: ",
      round(prob$arrow, 3)
    )
    
  })
  
  output$probability_dart <- renderText({
    
    model <- model_selected()
    
    if (is.null(model)) {
      return("Probability of dart: —")
    }
    
    if (!is.na(input$length) &&
        !is.na(input$width) &&
        !is.na(input$thickness)) {
      
      newdata <- data.frame(
        length = input$length,
        width = input$width,
        thickness = input$thickness
      )
      
      
    } else if (!is.na(input$length) &&
               !is.na(input$width)) {
      
      newdata <- data.frame(
        length = input$length,
        width = input$width
      )
      
      
    } else if (!is.na(input$width) &&
               !is.na(input$thickness)) {
      
      newdata <- data.frame(
        width = input$width,
        thickness = input$thickness
      )
      
    }
    
    prob <- predict(model, newdata = newdata, type = "prob")
    
    paste0(
      "Probability of dart: ",
      round(prob$dart, 3)
    )
    
  })
  
  output$probability_plot <- renderPlot({
    
    model <- model_selected()
    
    if (is.null(model)) {
      return(NULL)
    }
    
    if (!is.na(input$length) &&
        !is.na(input$width) &&
        !is.na(input$thickness)) {
      
      newdata <- data.frame(
        length = input$length,
        width = input$width,
        thickness = input$thickness
      )
      
    } else if (!is.na(input$length) &&
               !is.na(input$width)) {
      
      newdata <- data.frame(
        length = input$length,
        width = input$width
      )
      
    } else if (!is.na(input$width) &&
               !is.na(input$thickness)) {
      
      newdata <- data.frame(
        width = input$width,
        thickness = input$thickness
      )
      
    }
    
    prob <- predict(model, newdata = newdata, type = "prob")
    
    plot_data <- data.frame(
      Type = c("Arrow", "Dart"),
      Probability = c(
        prob$arrow,
        prob$dart
      )
    )
    
    ggplot(plot_data, aes(x = Type, y = Probability)) +
      geom_col(width = 0.6) +
      scale_y_continuous(
        limits = c(0, 1),
        labels = scales::percent
      ) +
      labs(
        x = NULL,
        y = "Probability"
      ) +
      theme_classic(base_size = 14)
    
  })
  
}
# Run the application 
shinyApp(ui = ui, server = server)

