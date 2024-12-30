import { Injectable } from '@angular/core';
import exp from 'constants';
import { Observable,of } from 'rxjs';
import { provideHttpClient, HttpClient, HttpParams } from '@angular/common/http';
import { map } from 'rxjs/operators';

export interface ListConsultation {
  date: string;
  NConsultation: number;
  Ordo:string;
  Bilan_bio:string;
  Bilan_rad:string;
  Resume: string;
}

export interface ListMeds {
  Medicament : string ;
  Dose : string ;
  Duree : string ;
  
  }

  export interface ListSoins {
    Date:String;
    Description:string;
    Observation:string;
  }

  export interface ConsultationData {
    num_consult: number;
    date_consult: string;
    ordonnance: boolean;
    prescription: boolean;
    resume: boolean;
  }

@Injectable({
  providedIn: 'root'
})
export class ConsulterDpiService {

  private ELEMENT_DATA: ListConsultation[] = [
    { NConsultation: 1, date: '16/12/2024', Ordo: 'oui', Bilan_bio: 'non',Bilan_rad:'oui', Resume: 'oui' },
    { NConsultation: 2, date: '21/12/2024', Ordo: 'oui', Bilan_bio: 'oui',Bilan_rad:'oui', Resume: 'oui' },
    { NConsultation: 3, date: '21/12/2024', Ordo: 'non', Bilan_bio: 'non',Bilan_rad:'oui', Resume: 'oui' },
    { NConsultation: 3, date: '21/12/2024', Ordo: 'oui', Bilan_bio: 'non',Bilan_rad:'non', Resume: 'oui' },
    { NConsultation: 4, date: '21/12/2024', Ordo: 'non', Bilan_bio: 'oui',Bilan_rad:'oui', Resume: 'oui' },
    { NConsultation: 5, date: '21/12/2024', Ordo: 'non', Bilan_bio: 'non',Bilan_rad:'non', Resume: 'non' },
  ];

 private  soins: ListSoins[] = [
  {
    Date: "2024-12-21",
    Description: "Consultation médicale ",
    Observation: "Rien à signaler"
  },
  {
    Date: "2024-12-20",
    Description: "Suivi post-opératoire",
    Observation: "Guérison satisfaisante"
  },
  {
    Date: "2024-12-19",
    Description: "Vaccination antigrippale",
    Observation: "Pas d'effets secondaires"
  },
  {
    Date: "2024-12-18",
    Description: "Prise de sang",
    Observation: "Résultats normaux"
  },
  {
    Date: "2024-12-17",
    Description: "Radiographie pulmonaire ",
    Observation: "Aucune anomalie détectée"
  }
];

  private ELEMENT_DATA_med : ListMeds[] = [
    {
      Medicament: 'Paracétamol',Dose: '500mg',Duree: '3 fois par jour pendant 5 jours'
    },
    {
      Medicament: 'Ibuprofène',Dose: '200mg',Duree: '2 fois par jour pendant 7 jours'
    },
    {
      Medicament: 'Amoxicilline',Dose: '250mg', Duree: '3 fois par jour pendant 7 jours'
    }
  ];
  private valeurBio =  { Pression_arterielle: '120/80', Glycemie: '1.2 g/L', Niveau_cholesterol: '200 mg/dL' };

  private apiUrl = 'http://127.0.0.1:8000/api/miseajourdpi/getConsultations/';
  private soinsurl = 'http://127.0.0.1:8000/api/miseajourdpi/getSoins/';
  constructor(private http: HttpClient) { }
/*
  getListConsultation(dpi: number):Observable<any>{
    const params = new HttpParams().set('dpi', dpi.toString());
    return  this.http.get<any>(this.apiUrl, { params });
  }*/
   getListConsultation(dpi: number): Observable<ListConsultation[]> {
      const params = new HttpParams().set('dpi', dpi);
      console.log("hi");
      return this.http.get<ConsultationData[]>(this.apiUrl, { params }).pipe(
        map((data: ConsultationData[]) => 
          data.map(consultation => ({
            NConsultation: consultation.num_consult,        // num_consult -> NConsultation
            date: consultation.date_consult,                // date_consult -> date
            Ordo: consultation.ordonnance ? 'oui' : 'non',  // ordonnance -> Ordo (oui/non)
            Bilan_bio: 'non',                              // Utiliser vos propres données pour Bilan_bio
            Bilan_rad: 'non',                              // Utiliser vos propres données pour Bilan_rad
            Resume: consultation.resume ? 'oui' : 'non'    // resume -> Resume (oui/non)
          }))
        )
      );
    }
    
  getListMeds():Observable<ListMeds[]>{
     return of(this.ELEMENT_DATA_med);
  }
  getValeurBio():Observable<{ Pression_arterielle: string; Glycemie: string; Niveau_cholesterol: string }>{
    return of(this.valeurBio);
  }
  getListSoins():Observable<ListSoins[]>{
    return of(this.soins);
  }
   
}
