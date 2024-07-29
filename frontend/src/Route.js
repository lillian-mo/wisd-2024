import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import {VizPage} from './pages/viz.js';
import { AnalysisPage } from './pages/analysis.js';

export const Routes = () => {
    return(
        <Routes>
        <Route path="/" element={<VizPage />}>
          <Route path="/analysis" element={<AnalysisPage />} />
        </Route>
      </Routes>
    );
}



