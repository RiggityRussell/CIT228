using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Data;
using System.Windows;

namespace ValueConverter.Converters
{
    public class BoolToVisibilityConverter : IValueConverter // added System.Windows.Data
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture) //We care about the object value.
        {
            var booleanVal = (bool)value; //Converts whatever we pass to a boolean
            if (booleanVal)
                return Visibility.Visible; // added System.Windows
            else
                return Visibility.Hidden;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
