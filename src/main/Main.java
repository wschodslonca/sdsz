package main;
import java.io.File;
import java.lang.String;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;
import javafx.application.Application;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.scene.text.Text;
import javafx.scene.*;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.*;
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


    private static int YEARL = 2000; // year of legit data
    private static int YEARS = 2000; // year of simulated data
    //imgs

    private static final String EARTH_MAP_IMG = "/resources/img/earthMap.jpg";
    private static final String COLOUR_SCALE = "/resources/img/colourscale.jpg";
    private static final String TEST = "/resources/img/earth288.png";
    private static final int [] yearsInt = IntStream.rangeClosed(1978, 2020).toArray();
    private static final String[] years = new String[43];
    private static String NASA_IMG_PATH_LEGIT = "", NASA_IMG_PATH_SIM = "";

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
    public void start(Stage primaryStage) throws Exception {

        BorderPane root = new BorderPane();
        root.getStyleClass().add("borderPane");
        GridPane gridPane = new GridPane();
        Pane p1 = new Pane();
        Pane p2 = new Pane();
        p1.getStyleClass().add("pane1");
        p2.getStyleClass().add("pane2");
        VBox vbox = new VBox();
        vbox.getStyleClass().add("vbox");
        gridPane.getStyleClass().addAll("gridpane","grid");

        Sphere s1 = new Sphere(RADIUS);
        Sphere s2 = new Sphere(RADIUS);
        s2.getStyleClass().add("s2");
        Group group1 = new Group();
        Group group2 = new Group();
        gridPane.getChildren().add(p1);
        gridPane.getChildren().add(p2);
        group1.getChildren().add(s1);
        group2.getChildren().add(s2);
        group1.getStyleClass().add("g1");
        group2.getStyleClass().add("g2");
        GridPane.setConstraints(p1, 0, 1);
        GridPane.setConstraints(p2, 1, 1);
        p1.getChildren().add(group1);
        p2.getChildren().add(group2);


        PhongMaterial mat = new PhongMaterial();
        AtomicInteger imgNr = new AtomicInteger(0);

        NASA_IMG_PATH_LEGIT = setLegitPath(YEARL);
        NASA_IMG_PATH_SIM = setSimPath(YEARL);
        final File[][] fileL = {getFiles()};
        final String[] pathLegit = {""};
        final String[] pathSim = { "" };
        pathLegit[0] = setLegitFilePath(fileL[0]);
        pathSim[0] = setSimFilePath(fileL[0]);
        for ( int i = 0; i < 43; i++) years[i] = String.valueOf(yearsInt[i]);

        ImageHolder imgHolderL = new ImageHolder(pathLegit[0]);
        ImageHolder imgHolderS = new ImageHolder(pathSim[0]);
        ImageHolder scale = new ImageHolder(COLOUR_SCALE);
        scale.setImage(new Image(getClass().getResourceAsStream(COLOUR_SCALE)));
        ImageView scaleImg = new ImageView();
        scaleImg.setImage(scale.getImg());
        imgHolderL.setImage(new Image(getClass().getResourceAsStream(pathLegit[0])));
        imgHolderS.setImage(new Image(getClass().getResourceAsStream(pathSim[0])));
        ImageView legitImg = new ImageView();
        legitImg.setImage(imgHolderL.getImg());
        ImageView simImg = new ImageView();
        simImg.setImage(imgHolderS.getImg());
        scaleImg.getStyleClass().add("scale");
        legitImg.getStyleClass().add("img2");
        simImg.getStyleClass().add("img1");
        gridPane.getChildren().addAll(legitImg,simImg);
        GridPane.setConstraints(legitImg,1,0);
        GridPane.setConstraints(simImg,0,0);
        Label currentYear = new Label("Current year: " + YEARL);
        Text simFootage = new Text("Simulated footage: ");
        Text actualFootage = new Text("Actual footage: ");
        simFootage.getStyleClass().add("simFoot");
        actualFootage.getStyleClass().add("actFoot");
        Text fileName = new Text(fileL[0][imgNr.get()].getName());
        fileName.getStyleClass().add("fileName");
        currentYear.getStyleClass().add("currentYear");
        gridPane.add(simFootage, 0, 0);
        gridPane.add(actualFootage, 1, 0);
        vbox.getChildren().add(currentYear);
        vbox.getChildren().add(fileName);

        ChoiceBox yearMenu = new ChoiceBox(FXCollections.observableArrayList(years));
        yearMenu.setValue(String.valueOf(YEARL));
        yearMenu.getStyleClass().add("yearMenu");
        yearMenu.getSelectionModel().selectedIndexProperty().addListener(new ChangeListener<Number>() {
            @Override
            public void changed(ObservableValue<? extends Number> observableValue, Number value, Number new_value) {
                YEARL = YEARS = yearsInt[new_value.intValue()];
                NASA_IMG_PATH_LEGIT = setLegitPath(YEARL);
                NASA_IMG_PATH_SIM = setSimPath(YEARL);
                pathLegit[0] = setLegitFilePath(fileL[0]);
                pathSim[0] = setSimFilePath(fileL[0]);
                fileL[0] = getFiles();
                currentYear.setText("Current year: " + YEARL);
                imgSwitch(mat, imgNr, fileL[0], imgHolderL, imgHolderS, legitImg, simImg, fileName);


            }
        });
        vbox.getChildren().add(yearMenu);
        Camera camera = new PerspectiveCamera(true);
        Scene scene = new Scene(root, WIDTH, HEIGHT);
        scene.getStylesheets().add("main/javafxstyles.css");
        scene.setCamera(new PerspectiveCamera());
        vbox.getChildren().add(scaleImg);

        root.setCenter(gridPane);
        root.setRight(vbox);

        group1.translateXProperty().set(70);
        group1.translateYProperty().set(180);
        group1.translateZProperty().set(500);

        group2.translateXProperty().set(600);
        group2.translateYProperty().set(180);
        group2.translateZProperty().set(500);

        mat.setDiffuseMap(imgHolderL.getImg());
        s1.setMaterial(mat);
        s2.setMaterial(mat);

        initMouseControl(group1);
        initMouseControl(group2);
        primaryStage.addEventHandler(KeyEvent.KEY_PRESSED,keyEvent -> {
            switch(keyEvent.getCode()) {
                case A:
                case LEFT:
                    if (imgNr.get() > 0) {
                        imgNr.getAndDecrement();
                        imgSwitch(mat, imgNr, fileL[0], imgHolderL, imgHolderS, legitImg, simImg, fileName);
                    }
                    break;
                case D:
                case RIGHT:
                    if (imgNr.get() < fileL[0].length-1) {
                        imgNr.getAndIncrement();
                        imgSwitch(mat, imgNr, fileL[0], imgHolderL, imgHolderS, legitImg, simImg, fileName);
                    }
                    break;
            }
        });
        primaryStage.setTitle("sdsz");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void imgSwitch(PhongMaterial mat, AtomicInteger imgNr, File[] fileL, ImageHolder imgHolderL, ImageHolder imgHolderS, ImageView legitImg, ImageView simImg, Text fileNameT) {
        imgHolderL.setImage(new Image(getClass().getResourceAsStream(NASA_IMG_PATH_LEGIT +fileL[imgNr.get()].getName())));
        imgHolderS.setImage(new Image(getClass().getResourceAsStream(NASA_IMG_PATH_SIM + fileL[imgNr.get()].getName())));
        mat.setDiffuseMap(imgHolderL.getImg());
        legitImg.setImage(imgHolderL.getImg());
        simImg.setImage(imgHolderS.getImg());
        fileNameT.setText(fileL[imgNr.get()].getName());
    }

    private File[] getFiles() {
        return new File(getClass().getResource(NASA_IMG_PATH_LEGIT).getPath()).listFiles();
    }

    private String setLegitPath(int YEARL) {
        String legit = "/resources/img/nasa/"+YEARL+"/";
        return legit;
    }

    private String setSimPath(int YEARL) {
        String sim = "/resources/img/base1985/"+YEARL+"/";
        return sim;
    }

    private String setLegitFilePath(File[] fileL) {
        String pathLegit = NASA_IMG_PATH_LEGIT+fileL[0].getName();
        return pathLegit;
    }

    private String setSimFilePath(File[] fileL) {
        String pathSim = NASA_IMG_PATH_SIM+fileL[0].getName();
        return pathSim;
    }


    public static void main(String[] args) {
        launch(args);
    }

}