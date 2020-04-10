package main;

import java.lang.String;
import javafx.application.Application;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.scene.*;
import javafx.scene.image.Image;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Sphere;
import javafx.scene.transform.Rotate;
import javafx.scene.transform.Transform;
import javafx.stage.Stage;

public class Main extends Application {

    class RotatingGroup extends Group{
        Rotate r;
        Transform t = new Rotate();
        public void rx(int angle) {
            r = new Rotate(angle,Rotate.X_AXIS);
            t = t.createConcatenation(r);
            this.getTransforms().clear();
            this.getTransforms().addAll(t);
        }
        public void ry(int angle) {
            r = new Rotate(angle,Rotate.Y_AXIS);
            t = t.createConcatenation(r);
            this.getTransforms().clear();
            this.getTransforms().addAll(t);
        }


    }

    //imgs
    private static final String EARTH_MAP_IMG = "/resources/img/earthMap.jpg";

    private static final int RADIUS = 50;
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private double anchX, anchY, anchAngX = 0,  anchAngY = 0;
    private final DoubleProperty angX = new SimpleDoubleProperty(0);
    private final DoubleProperty angY = new SimpleDoubleProperty(0);


    private void initMouseControl(RotatingGroup g, Scene scene) {
        Rotate xRot, yRot;
        g.getTransforms().addAll(
                xRot = new Rotate(0,Rotate.X_AXIS),
                yRot = new Rotate(0,Rotate.Y_AXIS)
        );
        xRot.angleProperty().bind(angX);
        yRot.angleProperty().bind(angY);
        scene.setOnMousePressed(event -> {
            anchX = event.getSceneX();
            anchY = event.getSceneY();
            anchAngX = angX.get();
            anchAngY = angY.get();
        });

        scene.setOnMouseDragged(event -> {
            angX.set(anchAngX - (anchY - event.getSceneY()));
          angY.set(anchAngY + (anchX - event.getSceneX()));
    });
}

    @Override
    public void start(Stage primaryStage) throws Exception{

        Sphere s = new Sphere(RADIUS);
        Group group = new Group(); // root group class
        RotatingGroup rg = new RotatingGroup(); // my class with rotating feature
        rg.getChildren().add(s);
        group.getChildren().add(rg);

        Camera camera = new PerspectiveCamera(true);
        Scene scene = new Scene(group, WIDTH, HEIGHT);
        scene.setFill(Color.NAVY);
        scene.setCamera(new PerspectiveCamera());

        rg.translateXProperty().set(WIDTH/2);
        rg.translateYProperty().set(HEIGHT/2);
        rg.translateZProperty().set(-800);


        PhongMaterial mat = new PhongMaterial();
        mat.setDiffuseMap(new Image(getClass().getResourceAsStream(EARTH_MAP_IMG)));
        s.setMaterial(mat);

        initMouseControl(rg,scene);
        primaryStage.setTitle("sdsz");
        primaryStage.setScene(scene);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }

}
