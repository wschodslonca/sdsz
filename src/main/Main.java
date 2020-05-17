package main;

import java.io.File;
import java.lang.String;
import java.util.concurrent.atomic.AtomicInteger;

import javafx.application.Application;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.scene.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Sphere;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;

public class Main extends Application {
    public class ImageHolder {
        Image im;
        ImageHolder(String path) {
            im = new Image(getClass().getResourceAsStream(path));
        }
        public Image getImg() {
            return this.im;
        }
        public void setImage(Image im) {
            this.im = im;
        }
    }


    private static final int YEARL = 2005; // year of legit data
    private static final int YEARS = 2005; // year of simulated data
    //imgs

    private static final String EARTH_MAP_IMG = "/resources/img/earthMap.jpg";
    private static final String TEST = "/resources/img/earth288.png";
    private static final String NASA_IMG_PATH_LEGIT = "/resources/img/nasa/"+YEARL+"/";
    private static final String NASA_IMG_PATH_SIM = "/resources/img/nasa/"+YEARS+"/";

    private static final int RADIUS = 180;
    private static final int WIDTH = 1024;
    private static final int HEIGHT = 768;
    private double anchX, anchY, anchAngX = 0,  anchAngY = 0;
    private final DoubleProperty angX = new SimpleDoubleProperty(0);
    private final DoubleProperty angY = new SimpleDoubleProperty(0);
    private static final int EARTHX = 100;
    private static final int EARTHY = 100;



    private void initMouseControl(Parent g) {
        Rotate xRot, yRot;
        g.getTransforms().addAll(
                xRot = new Rotate(0,Rotate.X_AXIS),
                yRot = new Rotate(0,Rotate.Y_AXIS)
        );
        xRot.angleProperty().bind(angX);
        yRot.angleProperty().bind(angY);
        g.setOnMousePressed(event -> {
            anchX = event.getSceneX();
            anchY = event.getSceneY();
            anchAngX = angX.get();
            anchAngY = angY.get();
        });

        g.setOnMouseDragged(event -> {
            angX.set(anchAngX - (anchY - event.getSceneY()));
          angY.set(anchAngY + (anchX - event.getSceneX()));
    });
}

    @Override
    public void start(Stage primaryStage) throws Exception{



        BorderPane root = new BorderPane();
        GridPane gridPane = new GridPane();
        Pane p = new Pane();
        p.getStyleClass().add("pane");

        VBox vbox = new VBox();
        vbox.getStyleClass().add("vbox");
        gridPane.getStyleClass().addAll("gridpane","grid");

        Sphere s = new Sphere(RADIUS);
        Group group = new Group(); // root group class
        gridPane.getChildren().add(p);
        group.getChildren().add(s);
        GridPane.setConstraints(p, 0, 1);
        p.getChildren().add(group);

        PhongMaterial mat = new PhongMaterial();
        AtomicInteger imgNr = new AtomicInteger(1);

        File[] fileL = new File(getClass().getResource(NASA_IMG_PATH_LEGIT).getPath()).listFiles();
        for (File f: fileL) {
            System.out.println(f.getName());
        }

        final String pathLegit = NASA_IMG_PATH_LEGIT+fileL[0].getName();
        final String pathSim = NASA_IMG_PATH_SIM+fileL[0].getName();



        ImageHolder imgHolderL = new ImageHolder(pathLegit);
        ImageHolder imgHolderS = new ImageHolder(pathSim);
        imgHolderL.setImage(new Image(getClass().getResourceAsStream(pathLegit)));
        imgHolderS.setImage(new Image(getClass().getResourceAsStream(pathSim)));
        ImageView legitImg = new ImageView();
        legitImg.setImage(imgHolderL.getImg());
        ImageView simImg = new ImageView();
        simImg.setImage(imgHolderS.getImg());
        gridPane.getChildren().addAll(legitImg,simImg);
        GridPane.setConstraints(legitImg,1,0);
        GridPane.setConstraints(simImg,0,0);

        Camera camera = new PerspectiveCamera(true);
        Scene scene = new Scene(root, WIDTH, HEIGHT);
        scene.getStylesheets().add("main/javafxstyles.css");
        scene.setFill(Color.GREY);
        scene.setCamera(new PerspectiveCamera());

        root.setCenter(gridPane);
        root.setRight(vbox);

        group.translateXProperty().set(70);
        group.translateYProperty().set(180);
        group.translateZProperty().set(500);

        mat.setDiffuseMap(imgHolderL.getImg());
        s.setMaterial(mat);

        initMouseControl(group);
        primaryStage.addEventHandler(KeyEvent.KEY_PRESSED,keyEvent -> {
            switch(keyEvent.getCode()) {
                case A:
                    if (imgNr.get() > 1) {
                        imgNr.getAndDecrement();
                        imgHolderL.setImage(new Image(getClass().getResourceAsStream(NASA_IMG_PATH_LEGIT +fileL[imgNr.get()].getName())));
                        imgHolderS.setImage(new Image(getClass().getResourceAsStream(NASA_IMG_PATH_SIM + fileL[imgNr.get()].getName())));
                        mat.setDiffuseMap(imgHolderL.getImg());
                        legitImg.setImage(imgHolderL.getImg());
                        simImg.setImage(imgHolderS.getImg());
                    }
                    break;
                case D:
                    if (imgNr.get() < fileL.length-1) {
                        imgNr.getAndIncrement();
                        imgHolderL.setImage(new Image(getClass().getResourceAsStream(NASA_IMG_PATH_LEGIT + fileL[imgNr.get()].getName())));
                        imgHolderS.setImage(new Image(getClass().getResourceAsStream(NASA_IMG_PATH_SIM + fileL[imgNr.get()].getName())));
                        mat.setDiffuseMap(imgHolderL.getImg());
                        legitImg.setImage(imgHolderL.getImg());
                        simImg.setImage(imgHolderS.getImg());
                    }
                    break;
            }
        });
        primaryStage.setTitle("sdsz");
        primaryStage.setScene(scene);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }

}
