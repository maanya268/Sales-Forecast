import {
  Component,
  ElementRef,
  EventEmitter,
  OnInit,
  Output,
  ViewChild,
} from '@angular/core';

@Component({
  selector: 'app-features',
  templateUrl: './features.component.html',
  styleUrls: ['./features.component.css'],
})
export class FeaturesComponent implements OnInit {
  
  constructor() {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    
  }
  featureData = [
    {
      image: '../../../assets/Images/predict.jpg',
      title: 'Predict',
      content:
        'Generate accurate sales predictions by analyzing sales records on a weekly, monthly, daily, or yearly basis. Utilize data processing techniques to extract meaningful insights and forecast future sales patterns.',
    },
    {
      image: '../../../assets/Images/visualise.png',
      title: 'Visualize',
      content:
        'Visualize the predicted values through bar and line charts, accompanied by comprehensive prediction metrics. Additionally, facilitate the download of the predicted data in CSV format.',
    },
    {
      image: '../../../assets/Images/save.png',
      title: 'Save',
      content:
        'Ensure the preservation of prediction metrics, visualizations, and predicted values for future reference and analysis.',
    },
  ];
}
